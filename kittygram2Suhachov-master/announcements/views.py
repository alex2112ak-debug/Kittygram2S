from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Announcement, Photo
from .serializers import AnnouncementSerializer, AnnouncementCreateUpdateSerializer, PhotoSerializer
from .permissions import IsOwnerOrReadOnly

class AnnouncementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['type', 'status']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return (
            Announcement.objects
            .select_related('owner')
            .prefetch_related('photos')
        )

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AnnouncementCreateUpdateSerializer
        return AnnouncementSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_create(self, serializer):
        """Устанавливает владельцем текущего пользователя."""
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsOwnerOrReadOnly])
    def close(self, request, pk=None):
        """Закрыть объявление (статус closed)."""
        announcement = self.get_object()
        if announcement.status == 'closed':
            return Response({'detail': 'Объявление уже закрыто.'}, status=status.HTTP_400_BAD_REQUEST)
        announcement.status = 'closed'
        announcement.save()
        return Response({'status': 'Объявление закрыто'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsOwnerOrReadOnly])
    def add_photo(self, request, pk=None):
        """Добавить фотографию к объявлению."""
        announcement = self.get_object()
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(announcement=announcement)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='photos', url_name='photos')
    def list_photos(self, request, pk=None):
        """Получить список фотографий объявления."""
        announcement = self.get_object()
        photos = announcement.photos.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
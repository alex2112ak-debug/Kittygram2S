from rest_framework import serializers
from django.core.validators import MinLengthValidator, FileExtensionValidator
from PIL import Image
from .models import Announcement, Photo

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png'],
                message='Допустимые форматы: JPEG, PNG.'
            )
        ]
    )

    class Meta:
        model = Photo
        fields = ('id', 'image', 'uploaded_at')
        read_only_fields = ('uploaded_at',)

    def validate_image(self, value):
        # Проверка размера файла (5 МБ)
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('Размер изображения не должен превышать 5 МБ.')
        # Дополнительная проверка через PIL
        try:
            img = Image.open(value)
            img.verify()
        except Exception:
            raise serializers.ValidationError('Файл не является корректным изображением.')
        return value


class AnnouncementSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'description', 'type', 'status',
                  'location', 'contact_info', 'owner', 'created_at',
                  'updated_at', 'photos')
        read_only_fields = ('owner', 'created_at', 'updated_at', 'status')


class AnnouncementCreateUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=200,
        validators=[MinLengthValidator(3, message='Заголовок должен содержать минимум 3 символа.')]
    )
    description = serializers.CharField(
        validators=[MinLengthValidator(10, message='Описание должно содержать минимум 10 символов.')]
    )

    class Meta:
        model = Announcement
        fields = ('title', 'description', 'type', 'location', 'contact_info')
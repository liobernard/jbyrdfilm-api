from rest_framework.serializers import (
    ModelSerializer, CharField,
    PrimaryKeyRelatedField,
)
from .models import HomeInfo, AboutInfo
from videos.models import Video
from videos.serializers import ThumbnailVideoSerializer

class HomeInfoSerializer(ModelSerializer):
    name = CharField(read_only=True, source='get_info_name')
    featured_video = ThumbnailVideoSerializer()

    class Meta:
        model = HomeInfo
        fields = (
            'name',
            'facebook_url',
            'instagram_url',
            'twitter_url',
            'logo_url',
            'video_banner_url',
            'featured_video',
            'info_1',
            'info_2',
        )

class PutHomeInfoSerializer(HomeInfoSerializer):
    featured_video = PrimaryKeyRelatedField(
        queryset=Video.objects.filter(
            published_at__isnull=False
        )
    )

class AboutInfoSerializer(ModelSerializer):
    name = CharField(read_only=True, source='get_info_name')

    class Meta:
        model = AboutInfo
        fields = (
            'name',
            'text',
            'photo_url',
            'showreel_url',
        )

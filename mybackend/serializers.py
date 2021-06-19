from rest_framework import serializers
from .models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = (
            'title',
            'year',
            'age_rating',
            'imdb_rating',
            'on_netflix'
        )

from django.contrib import admin
from .models import App


class AppAdmin(admin.ModelAdmin):
    list = (
        'title',
        'year',
        'age_rating',
        'imdb_rating',
        'on_netflix'
    )


admin.site.register(App, AppAdmin)

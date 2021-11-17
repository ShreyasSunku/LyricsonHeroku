from django.contrib import admin
from . import models
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(models.YouTube, MyModelAdmin)
admin.site.register(models.Movie)
admin.site.register(models.Lyrics)
admin.site.register(models.Actor)
admin.site.register(models.MovieDirector)
admin.site.register(models.MusicDirector)
admin.site.register(models.Studio)
admin.site.register(models.Producer)
admin.site.register(models.Country)
admin.site.register(models.Wood)
admin.site.register(models.Language)
admin.site.register(models.Genre)
admin.site.register(models.Certificate)
admin.site.register(models.Singer)
admin.site.register(models.Logo)
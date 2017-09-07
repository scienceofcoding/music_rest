from django.contrib import admin
from .models import *

# Register your models here.


"""
for admin user:
username: root
password: qwertyuio
"""

class MusicianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'instrument', ]
    fields = ['first_name', 'last_name', 'instrument', ]

admin.site.register(Musician, MusicianAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['artist', 'name', 'release_date', 'num_stars', ]
    fields = ['artist', 'name', 'release_date', 'num_stars', ]
    
admin.site.register(Album, AlbumAdmin)


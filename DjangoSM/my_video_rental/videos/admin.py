from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']

    search_fields = ['title','length']

    list_filter = ['release_year','length','title']

    list_display = ['title','release_year','length']
# you can sort by clicking on the list headings in the list view

 # list_display is required for list_editable, ie , something needs to be displayed to be edited
    list_editable = ['length']

admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer)

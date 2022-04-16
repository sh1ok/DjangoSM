from django.contrib import admin
from . import models


class GroupMemberInLine(admin.TabularInline):
    models = models.GroupMember

admin.site.register(models.Group)

# Register your models here.

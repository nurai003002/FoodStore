from django.contrib import admin
from apps.base import models
from django.contrib.auth.models import User,Group
# Register your models here.

admin.site.register(models.Settings)
admin.site.unregister(User)
admin.site.unregister(Group)
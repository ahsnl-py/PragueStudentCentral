from django.contrib import admin
from .models import (
    UserProfile,
)

# Register your models here.

@admin.register(UserProfile)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('user','user_department')
    readonly_fields=('id',)

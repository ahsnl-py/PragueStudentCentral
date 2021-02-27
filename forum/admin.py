from django.contrib import admin
from .models import (
    Post, 
    Department, 
    Subject,
    #PostImage,
    #PostFile
    Notif_User,
    UploadFiles,
)

# Department view in admin 
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    ordering = ('department_name', )
    prepopulated_fields = {'department_slug': ('department_name',)}

# Subject view in admin 
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_filter = ('department_name', )
    ordering = ('subject_name', 'department_name', )
    prepopulated_fields = {'subject_slug': ('subject_name',)}
    

# Post view in admin 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {
                            'slug': ('title',)
                          }
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Notif_User)
class DepartmentAdmin(admin.ModelAdmin):
    ordering = ('user_email', )
    # prepopulated_fields = {'department_slug': ('department_name',)}

@admin.register(UploadFiles)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('feed', 'file_upload')
    ordering = ('file_upload', )
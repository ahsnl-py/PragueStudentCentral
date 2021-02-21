from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('',views.home, name='forum-home'),    
    path('about/', views.about, name='forum-about'),
    path('post/', views.post_list, name='forum_post_list'),
    path('new_post/', views.new_post, name='new_post'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:dept_id>/', views.subject_dept, name='subject'),
    path('departments/<int:dept_id>/<int:subject_name_id>', views.post_subject_dept, name='post_by_subject'),
    #path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',views.TEST_post_detail,name='post_detail'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
]
from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('',views.home, name='forum-home'),
    path('departments/', views.departments, name='departments'),
    path('departments/<single_slug>', views.single_slug, name='single_slug'),
    path('about/', views.about, name='forum-about'),
    path('post/', views.post_list, name='forum_post_list'),
    path('new_post/', views.new_post, name='new_post'),
    #path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',views.TEST_post_detail,name='post_detail'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
]
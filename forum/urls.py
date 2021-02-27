from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('',views.home, name='forum-home'),    
    path('about/', views.about, name='forum-about'),
    path('post/', views.post_list, name='post_list'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:dept_id>/', views.subject_dept, name='subject'),
    path('departments/<int:dept_id>/<int:subject_name_id>', views.post_subject_dept, name='post_by_subject'),
    path('new_post/', views.PostCreateView.as_view(), name='new_post'),
    #Test class list view path('post/', views.InventoryListView.as_view(), name='post_list'),
    path('post/<int:pk>/<slug:post>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/<slug:post>/update/', views.PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/<slug:post>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
]

"""OLD PATH"""
# path('new_post/', views.new_post, name='new_post'),
# path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',views.TEST_post_detail,name='post_detail'),
# path('post/<pk>/',views.TEST_post_detail,name='post_detail'),
# path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
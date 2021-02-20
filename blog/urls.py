from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreatelView,PostUpdatelView,PostDeletelView,UserPostListView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', PostListView.as_view() ,name = "blog_home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user_posts"),
    path('post/<int:pk>/delete/', PostDeletelView.as_view() ,name = "post_delete"),
    path('post/<int:pk>/update/', PostUpdatelView.as_view(), name="post_update"),
    path('post/<int:pk>', PostDetailView.as_view() ,name = "post_detail"),
    path('post/new/', PostCreatelView.as_view() ,name = "post_create"),
    path('about/', views.about ,name = "blog_about"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
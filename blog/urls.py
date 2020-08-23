from django.urls import path, re_path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView, FrontendRenderView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]

"""urlpatterns += [
	re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
]
#django no logner handles 404 errors, frontend does

# <app>/<model>_<viewtype>.html"""
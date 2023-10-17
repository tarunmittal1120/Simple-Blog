
from django.urls import path,include
from .views import HomeView,ArticleDetailsView,AddPostsView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,LikeView,AddCommentView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailsView.as_view(),name='article_detail'),
    path('addposts/',AddPostsView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('addcategory/',AddCategoryView.as_view(),name='add_category'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name='add_comment'),
    

]
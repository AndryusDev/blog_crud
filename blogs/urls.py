from django.urls import path
from .views import PostListView, PostDetailView,PostNewView,PostUpdateView, PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostNewView.as_view(), name="post-new"),
    path("post/<int:pk>/editar",PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/borrar",PostDeleteView.as_view(), name="post-delete"),
    ]

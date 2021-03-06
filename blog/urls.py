from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="postcreate"),
    path("draft/", views.PostDraft.as_view(), name="draft"),
    path("<int:pk>/", views.PostDetails.as_view(), name="postdetails"),
    path("comment/", views.CommentList.as_view(), name="comment"),
    path("comments/<int:pk>/", views.CommentDetails.as_view(), name="commentdetails"),
]

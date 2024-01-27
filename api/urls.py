from django.urls import path
from .views import BlogListCreateAPIView, BlogRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('blog/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blog/<uuid:id>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-retrieve-update-destroy'),
]

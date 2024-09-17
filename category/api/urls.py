from django.urls import path
from .views import CatApiView, CatUpdateDeleteView


urlpatterns = [
    path('cat-get-post', CatApiView.as_view(), name="cat-get-post"),
    path('cat-up-del/<int:pk>', CatUpdateDeleteView.as_view(), name="cat-up-del"),
]
    
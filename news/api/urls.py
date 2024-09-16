from django.urls import path
from .views import news, tags, tag_post, tag_stats, tag_detail, tag_update, tag_delete, TagApiView, UpdateAndDeleteView, news_today, news_today_create

urlpatterns = [
    path('', news, name="name"),
    path('tags', tags, name="tags"),
    path('tag-post', tag_post, name="tag-post"),
    path('tag-stats', tag_stats, name="tag-stats"),
    path('tag-detail', tag_detail, name="tag-detail"),
    path('tag-update', tag_update, name="tag-update"),
    path('tag-delete', tag_delete, name="tag-delete"),
    path('class-tag', TagApiView.as_view(), name="tag-view"),
    path('class-tag-update/<int:pk>', UpdateAndDeleteView.as_view(), name="tag-view-update"),
    path('today', news_today, name="news-today"),
    path('today-create', news_today_create, name="news-today-create"),
]
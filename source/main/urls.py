from django.contrib import admin
from django.urls import path
# from webapp.views import index_view, article_view, article_create_view, article_update_view, article_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", index_view, name="index"),
    # path("article/<int:pk>/", article_view, name="article_view"),
    # path("article/add/", article_create_view, name="article_add"),
    # path("article/<int:pk>/edit", article_update_view, name="article_update"),
    # path('article/<int:pk>/delete', article_delete_view, name="article_delete")
]
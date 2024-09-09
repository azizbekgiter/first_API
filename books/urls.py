from django.urls import path, include
from rest_framework import routers
from .views import AuthorModelView, CategoryModelView, BookModelView

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelView)
router.register(r'category', CategoryModelView)
router.register(r'book', BookModelView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls))
]

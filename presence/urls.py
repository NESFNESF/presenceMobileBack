from  django.urls import path , include
from rest_framework.routers import DefaultRouter
from  .views import ClassesTestViewSet
router = DefaultRouter()
router.register(r'classes',ClassesTestViewSet , basename='classes')

urlpatterns = [
    path("api/",include(router.urls))
]
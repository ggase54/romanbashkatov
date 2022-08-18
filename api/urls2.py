from django.urls import path, include
from rest_framework import routers
from .views import CheckboxViewSet

router = routers.DefaultRouter()
router.register('checkbox', CheckboxViewSet)

urlpatterns = [
  path('api/', include(router.urls))
]
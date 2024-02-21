from rest_framework import routers, serializers, viewsets
from .views import UserView, ReviewView


router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'reviews', ReviewView)
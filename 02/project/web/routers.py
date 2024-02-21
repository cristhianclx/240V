from rest_framework import routers, serializers, viewsets
from .views import UserView


router = routers.DefaultRouter()
router.register(r'users', UserView)
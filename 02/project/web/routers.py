from rest_framework import routers, serializers, viewsets
from .views import UserView, ReviewView, ReviewDetailView, EditionView


router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'reviews', ReviewView)
router.register(r'reviews/(?P<review_id>.+)/details', ReviewDetailView, basename="review-details")
router.register(r'editions', EditionView)
from django.urls import include, path
from rest_framework import routers

from image_processing.views import BusinessCardViewSet

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

router = routers.DefaultRouter()
router.register(r'business-card', BusinessCardViewSet,
                basename='business-card')
urlpatterns = router.urls

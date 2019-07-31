from django.urls import include, path
from rest_framework import routers
from image_processing.views import BusinessCardView
from image_processing import urls
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('business-card/', include(urls)),
]

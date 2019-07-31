from django.urls import path
from .views import BusinessCardView

urlpatterns = [
    path('', BusinessCardView.as_view())
]

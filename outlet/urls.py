from django.urls import path

from .views import OutletListView

urlpatterns = [
    path('', OutletListView.as_view(), name='list-outlet')
]

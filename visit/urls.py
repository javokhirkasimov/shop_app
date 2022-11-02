from django.urls import path

from .views import CreateVisitView

urlpatterns = [
    path('', CreateVisitView.as_view(), name='create-visit')
]

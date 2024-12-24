from django.urls import path
from django.views.generic import TemplateView
from .views import StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView

urlpatterns = [
    path('staff/', StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staff/create/', StaffCreateView.as_view(), name='staff_create'),
    path('staff/<int:pk>/update/', StaffUpdateView.as_view(), name='staff_update'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),
]

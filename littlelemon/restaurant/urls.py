from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemView.as_view(), name='menu-list-create'),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail-update-delete'),
    path('api-token-auth/', obtain_auth_token),
]
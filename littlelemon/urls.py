from django.urls import path,include
from .views import BookingsView,MenuItemsView,MenuItemView
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'tables', views.BookingsView)

urlpatterns=[
    path('menu',MenuItemsView.as_view() ),

    path('menu/<int:pk>', MenuItemView.as_view(), name="book-detail"),
    path('',include(router.urls) ),

]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserView, ChatGPTView, ObtainJWTTokenView, ReminderViewSet, ChatGPTViewDetail


urlpatterns = [   
    path('v1.0/signup/', CreateUserView.as_view(), name='signup'),
    path('v1.0/conversation/', ChatGPTView.as_view(), name='conversation'),
    path('v1.0/conversation/detail', ChatGPTViewDetail.as_view(), name='conversation'),
    path('v1.0/api/token/', ObtainJWTTokenView.as_view(), name='obtain_jwt_token'),
    path('reminders.app/', ReminderViewSet.as_view({'get': 'list'}), name='teste'),
]

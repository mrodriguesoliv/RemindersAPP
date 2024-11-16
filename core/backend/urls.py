from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import CreateUserView, ChatGPTView, ReminderViewSet, ChatGPTViewDetail



urlpatterns = [   
    path('v1.0/signup/', CreateUserView.as_view(), name='signup'),
    path('v1.0/conversation/', ChatGPTView.as_view(), name='conversation'),
    path('v1.0/conversation/detail', ChatGPTViewDetail.as_view(), name='conversation'),
    path('v1.0/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('reminders.app/', ReminderViewSet.as_view({'get': 'list'}), name='teste'),
]
    
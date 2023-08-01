from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserListView, UserDetailView
from users.api import views as api_views


app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]

router = SimpleRouter()
router.register('api', api_views.UserModelViewSet)

urlpatterns += router.urls
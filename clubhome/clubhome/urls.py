from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from rooms.views import RoomListView, RoomCreateView, RoomCreateWithUserView
from rooms.views_api import RoomViewSet
from users.views import UserProfileView, UserProfileGenericView
from users.views_api import UserViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', RoomListView.as_view(), name='room-list'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    path('users/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('users/details/<str:username>/', UserProfileGenericView.as_view(), name='user-profile-generic'),
    path('rooms/', RoomCreateView.as_view(), name='room-create'),
    path('rooms/create/', RoomCreateWithUserView.as_view(), name='room-create-with-user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

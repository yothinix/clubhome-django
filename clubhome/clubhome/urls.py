"""clubhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rooms.views import RoomListView, RoomCreateView, RoomCreateWithUserView
from users.views import UserProfileView, UserProfileGenericView

urlpatterns = [
    path('', RoomListView.as_view(), name='room-list'),
    path('admin/', admin.site.urls),
    path('users/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('users/details/<str:username>/', UserProfileGenericView.as_view(), name='user-profile-generic'),
    path('rooms/', RoomCreateView.as_view(), name='room-create'),
    path('rooms/create/', RoomCreateWithUserView.as_view(), name='room-create-with-user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

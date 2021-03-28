from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
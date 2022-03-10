from appuser.models import AppUser
from users.settings import CACHE_TTL
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView
from .pagination import CustomLimitOffsetPagination
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)


class UserList(ListAPIView):
    queryset=AppUser.objects.all()
    serializer_class = UserSerializer
    filterset_fields=['id']
    pagination_class = CustomLimitOffsetPagination

    

    





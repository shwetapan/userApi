from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):

    default_limit = 20
    max_limit = 30
    min_limit = 5
    min_offset = 0
  
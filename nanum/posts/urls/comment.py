from django.conf.urls import url, include

from .. import apis

__all__ = (
    'urlpatterns',
)

urlpatterns = [
    url(r'^$', apis.CommentAPI.as_view(), name='comment'),
]
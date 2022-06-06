from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import PostList, GroupList, CommentViewSet, FollowModul

# Создаётся роутер
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register(r'posts', PostList)
router.register(r'groups', GroupList)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename=CommentViewSet)
router.register(r'follow', FollowModul)

# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('v1/', include(router.urls)),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]

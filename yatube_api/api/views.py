from posts.models import Post, Group, Comment, Follow
from .serializers import (PostSerializer, GroupSerializer, CommentSerializer,
                          FollowSerializer)
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import filters
from .permissions import UserOrReadOnly, ReadOnly
from rest_framework.pagination import LimitOffsetPagination


class ListCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """"Микс на создание и чтение для подписчиков"""

    pass


class FollowModul(ListCreateViewSet):
    """Подписчики"""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset


class GroupList(viewsets.ReadOnlyModelViewSet):
    """Группы"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (UserOrReadOnly,)

    def get_permissions(self):
        # Если в GET-запросе требуется получить информацию об объекте
        if self.action == 'retrieve':
            # Вернем обновленный перечень используемых пермишенов
            return (ReadOnly(),)
    # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
        return super().get_permissions()


class PostList(viewsets.ModelViewSet):
    """Посты"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (UserOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        # Если в GET-запросе требуется получить информацию об объекте
        if self.action == 'retrieve':
            # Вернем обновленный перечень используемых пермишенов
            return (ReadOnly(),)
    # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    """Комментарии"""

    serializer_class = CommentSerializer
    permission_classes = (UserOrReadOnly,)

    def get_permissions(self):
        # Если в GET-запросе требуется получить информацию об объекте
        if self.action == 'retrieve':
            # Вернем обновленный перечень используемых пермишенов
            return (ReadOnly(),)
    # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
        return super().get_permissions()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user,
                        post=post)

    def get_queryset(self):
        # Получаем id поста из эндпоинта
        pk = self.kwargs.get('post_id')
        # И отбираем только нужные комментарии
        new_queryset = Comment.objects.filter(post=pk)
        return new_queryset

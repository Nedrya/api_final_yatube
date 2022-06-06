from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Post, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        many=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

        validators = [UniqueTogetherValidator(queryset=Follow.objects.all(),
                                              fields=('following', 'user'),
                                              message='Ты уже подписан.')]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return data


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = serializers.CharField(read_only=False, required=False)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post
        read_only_fields = ('pub_date',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment
        read_only_fields = ('created',)

    validators = [UniqueTogetherValidator(queryset=Comment.objects.all(),
                                          fields=('text',),
                                          message='Придумай что то другое :)')]

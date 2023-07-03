from rest_framework import serializers
from api.models import user,post,like

class userserializers(serializers.HyperlinkedModelSerializer):
    user_id=serializers.ReadOnlyField()
    class Meta:
        model=user
        fields="__all__"

class postserializers(serializers.HyperlinkedModelSerializer):
    post_id=serializers.ReadOnlyField()
    class Meta:
        model=post
        fields="__all__"

class likeserializers(serializers.HyperlinkedModelSerializer):
    like_id=serializers.ReadOnlyField()
    class Meta:
        model=like
        fields="__all__"
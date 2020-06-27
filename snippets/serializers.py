from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.Serializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    highlight=serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')
    class Meta:
        model = Snippet
        fields = ('url','id','highlight','owner', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    snippets=serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
    class Meta():
        model=User
        fields=('url','id','username','snippets')
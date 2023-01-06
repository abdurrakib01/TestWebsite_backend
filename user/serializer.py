from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=('id', 'name', 'sector', 'tc')
        
    def validate(self, attrs):
        tc = attrs.get('tc')
        if tc != True:
            raise serializers.ValidationError("Please agree to the terms")
        return attrs
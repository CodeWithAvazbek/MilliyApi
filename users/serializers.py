from rest_framework import serializers
from .models import UserModel


class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


from rest_framework import serializers


class UserRequestSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        help_text="User's full name",
    )


class UserDataSerializer(serializers.Serializer):
    username = serializers.CharField()


class UserResponseSerializer(serializers.Serializer):
    data = UserDataSerializer()
    message = serializers.CharField()


class ErrorResponseSerializer(serializers.Serializer):
    error = serializers.CharField()

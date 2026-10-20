from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField

User = get_user_model()

class UserRegistrationSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("username", "email", "password", "role")
        extra_kwargs = {
            "email": {"required": True},
            "role": {"required": False},
        }

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
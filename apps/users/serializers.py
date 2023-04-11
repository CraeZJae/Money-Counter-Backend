from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from secrets import token_hex
import datetime

class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = User
        fields = '__all__'

class UserSignUpSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(read_only = True)
    password = serializers.CharField(write_only = True, required = True)
    name = serializers.CharField(write_only = True)
    token = serializers.CharField(read_only = True)
    email = serializers.EmailField(write_only = True)
    token_expires = serializers.DateTimeField(read_only = True)

    class Meta:
        model=User
        fields = ('id', 'name', 'profile', 'email', 'password', 'token', 'token_expires')
        
    def create(self, validated_data):
        if User.objects.filter(email = validated_data["email"]).exists():
            raise serializers.ValidationError({"email": ["this email already exists, please login to continue"]})
        validated_data["password"] = make_password(validated_data["password"])
        validated_data['token'] = token_hex(30)
        validated_data["token_expires"] = datetime.datetime.now()+datetime.timedelta(days= 21)
        return super().create(validated_data)

class UserSignInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)
    profile = serializers.ImageField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'profile', 'email', 'password', 'token', 'token_expires')

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        if len(user) > 0 and check_password(validated_data['password'], user[0].password):
            user[0].token = token_hex(30)
            user[0].token_expires = datetime.datetime.now() + datetime.timedelta(days=7)
            user[0].save()

            return user[0]
        else:
            raise serializers.ValidationError({"error": "The password or email you enter is incorrect."})

class UserUpdateSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(required=False)

    def validate(self, data):
        errors = {}
        if 'name' not in data or not data['name']:
            errors['name'] = ['name is required.']

        if 'email' not in data or not data['email']:
            errors['email'] = ['email is required.']

        if bool(errors):
            raise serializers.ValidationError(errors)

        return data

    class Meta:
        model = User
        fields = ('id', 'name', 'profile', 'email', 'token', 'token_expires')

class UserUpdateBudgetSerializer(serializers.ModelSerializer):
    def validate(self, data):
        errors = {}
        if 'budget' not in data or not data['budget']:
            errors['budget'] = ['budget is required.']

        if bool(errors):
            raise serializers.ValidationError(errors)

        return data

    class Meta:
        model = User
        fields = ('id', 'budget')

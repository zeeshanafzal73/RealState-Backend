from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Property, Team, News, About, Agent, Messages, ContactUs

#Serializer to Register User


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    Token.objects.create(user=user)
    user.save()
    return user


class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()


class LatestProperty (serializers.ModelSerializer):
  class Meta:
    model = Property
    fields = '__all__'


class TeamSerializer (serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = News
    fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

  class Meta:
    model = About
    fields = '__all__'


class AgentSerializer (serializers.ModelSerializer):

  class Meta:
    model = Agent
    fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Messages
    fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactUs
    fields = '__all__'


class PasswordResetSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    LatestProperty,
    TeamSerializer,
    NewsSerializer,
    AboutSerializer,
    AgentSerializer,
    MessagesSerializer,
    ContactUsSerializer,
    PasswordResetSerializer,
)
from rest_framework import generics, status
from .models import Property, Team, News, About, Agent, Messages, ContactUs
from django.contrib.auth import update_session_auth_hash


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = LatestProperty


class LatestProperty(generics.ListAPIView):
    queryset = Property.objects.all().order_by("price")
    serializer_class = LatestProperty


class TeamDetailView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class Team(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class LatestNews(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class News(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class About(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AgentDetailView(generics.RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class Agent(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class Messages(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class ContactUs(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class PasswordResetAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        password2 = serializer.validated_data["password2"]

        user = User.objects.filter(username=username).first()

        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if password != password2:
            return Response(
                {"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(password)
        user.save()

        # Optionally, update the user's session authentication hash
        update_session_auth_hash(self.request, user)

        return Response(
            {"message": "Password reset successfully"}, status=status.HTTP_200_OK
        )

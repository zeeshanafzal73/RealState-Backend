from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('register/', views.RegisterUserAPIView.as_view(), name='register'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('property/', views.LatestProperty.as_view(), name='property'),
  path('team/', views.Team.as_view(), name='team'),
  path('news/', views.News.as_view(), name='news'),
  path('about/', views.About.as_view(), name='about'),
  path('agent/', views.Agent.as_view(), name='agent'),
  path('agent/<int:pk>/', views.AgentDetailView.as_view(), name='getAgent'),
  path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='getProperty'),
  path('news/<int:pk>/', views.LatestNews.as_view(), name='getNews'),
  path('messages/', views.Messages.as_view(), name='messages'),
  path("team/<int:pk>/", views.TeamDetailView.as_view(), name="getTeam"),
  path('contactus/', views.ContactUs.as_view(), name='ContactUs'),
  path('password_reset/', views.PasswordResetAPIView.as_view(), name='password_reset'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

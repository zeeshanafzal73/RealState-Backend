from django.contrib import admin
from .models import Property, Team, News, About, Agent, Messages, ContactUs
# Register your models here.

admin.site.register(Property)
admin.site.register(Team)
admin.site.register(News)
admin.site.register(About)
admin.site.register(Agent)
admin.site.register(Messages)
admin.site.register(ContactUs)

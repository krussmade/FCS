from django.contrib import admin
from .models import Profile, FAQ, Cat

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['tg_id', 'username', 'first_name', 'last_name']

admin.site.register(Profile, ProfileAdmin)

class FAQAdmin(admin.ModelAdmin):
	list_display = ['question']

admin.site.register(FAQ, FAQAdmin)
admin.site.register(Cat)
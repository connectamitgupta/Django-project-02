from django.contrib import admin
#from .models import social_contacts
#from .models import Social_Groups
from socialspace.models import social_contact
from socialspace.models import social_group

# Register your models here.

class social_contactAdmin(admin.ModelAdmin):
  list_display = ("person_name", "city", "mobile")
  prepopulated_fields = {"slug": ("person_name", "mobile")}

class social_groupAdmin(admin.ModelAdmin):
  list_display = ("group_name", "group_type", "social_media")
  prepopulated_fields = {"slug": ("social_media", "group_name")}

#admin.site.register(social_contacts,social_contactsAdmin)
#admin.site.register(Social_Groups)

admin.site.register(social_contact)
admin.site.register(social_group)
from django.db import models

# Create your models here.

class social_group(models.Model):
  MEDIA_OPTIONS = [
        ("WA", "Whatsapp"),
        ("FB", "Facebook"),
        ("TW", "Twitter"),
        ("LN", "Linked-in"),
    ]
  # id = models.IntegerField(primary_key=True, auto_increment=True)
  group_name = models.CharField(max_length=255)
  group_description = models.CharField(max_length=255)
  group_type = models.CharField(max_length=255)
  social_media = models.CharField(max_length=2,choices=MEDIA_OPTIONS, default='WA')
  created_on=models.DateField()


#   def __str__(self):
#     return f"{self.media} {self.group}"


class social_contact(models.Model):
  person_name = models.CharField(max_length=255)
  country_code = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255,unique=True) 
  city = models.CharField(max_length=255)
  # social_group_id = models.IntegerField()
  created_on=models.DateField()
  social_groups = models.ManyToManyField(social_group)


#   def __str__(self):
#     return f"{self.person_name} {self.mobile}"
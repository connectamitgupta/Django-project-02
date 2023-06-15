from django.db import models

# Create your models here.


class Social_Groups(models.Model):
  g_type = models.CharField(max_length=255)
  g_media = models.CharField(max_length=255)
  g_name = models.CharField(max_length=255)
  g_purpose = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.media} {self.group}"


class social_contacts(models.Model):
  person_name = models.CharField(max_length=255)
  country_code = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  social_group_id = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.person_name} {self.mobile}"
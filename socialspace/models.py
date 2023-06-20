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
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    return f"{self.group_name}"


class social_contact(models.Model):
  person_name = models.CharField(max_length=255)
  country_code = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255,unique=True) 
  city = models.CharField(max_length=255)
  # social_group_id = models.IntegerField()
  created_on=models.DateField()
  social_groups = models.ManyToManyField(social_group)
  slug = models.SlugField(default="", null=False)

  def __str__(self):
     return f"{self.mobile}     {self.city}"
  


## Added to test foreign key example from the following reference
## https://pythonprogramming.net/foreign-keys-django-tutorial/

  # class TutorialCategory(models.Model):
  #   tutorial_category = models.CharField(max_length=200)
  #   category_summary = models.CharField(max_length=200)
  #   category_slug = models.CharField(max_length=200, default=1)
  #   class Meta:
  #       # Gives the proper plural name for admin
  #       verbose_name_plural = "Categories"
  #   def __str__(self):
  #       return self.tutorial_category
    
  #   class TutorialSeries(models.Model):
  #     tutorial_series = models.CharField(max_length=200)
  #     tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
  #     series_summary = models.CharField(max_length=200)

  #     class Meta:
  #       # otherwise we get "Tutorial Seriess in admin"
  #       verbose_name_plural = "Series"

  #     def __str__(self):
  #       return self.tutorial_series
      
  #   class Tutorial(models.Model):
  #     tutorial_title = models.CharField(max_length=200)
  #     tutorial_content = models.TextField()
  #     tutorial_published = models.DateTimeField('date published')
  #     #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
  #     tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
  #     tutorial_slug = models.CharField(max_length=200, default=1)
  #     def __str__(self):
  #       return self.tutorial_title
# Generated by Django 4.2.2 on 2023-06-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trevitaessentials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('social_group_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='contacts',
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trevitaessentials', '0004_upload3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='upload4')),
            ],
        ),
    ]
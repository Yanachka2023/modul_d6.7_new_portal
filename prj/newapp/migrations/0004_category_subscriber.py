# Generated by Django 4.1.7 on 2023-04-28 20:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newapp', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscriber',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-17 09:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserDetail',
        ),
    ]

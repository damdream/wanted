# Generated by Django 3.2.8 on 2021-10-26 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user',
        ),
    ]

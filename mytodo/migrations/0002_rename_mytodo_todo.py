# Generated by Django 4.1 on 2022-11-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mytodo',
            new_name='todo',
        ),
    ]

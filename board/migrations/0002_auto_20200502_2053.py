# Generated by Django 3.0.5 on 2020-05-02 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Day',
            new_name='Topic',
        ),
    ]
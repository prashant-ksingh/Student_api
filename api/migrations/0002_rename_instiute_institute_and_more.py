# Generated by Django 4.2.3 on 2023-07-29 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instiute',
            new_name='Institute',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='instiute',
            new_name='insttiute',
        ),
    ]

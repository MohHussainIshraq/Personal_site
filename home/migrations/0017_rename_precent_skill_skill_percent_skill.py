# Generated by Django 4.1 on 2022-09-10 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='precent_skill',
            new_name='percent_skill',
        ),
    ]

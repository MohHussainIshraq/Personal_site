# Generated by Django 4.1 on 2022-09-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_about_description_alter_about_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

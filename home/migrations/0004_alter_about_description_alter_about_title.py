# Generated by Django 4.1 on 2022-09-10 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

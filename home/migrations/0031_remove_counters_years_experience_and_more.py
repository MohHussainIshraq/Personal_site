# Generated by Django 4.1 on 2022-09-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_counters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counters',
            name='years_experience',
        ),
        migrations.AlterField(
            model_name='counters',
            name='total_clients',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='counters',
            name='works_completed',
            field=models.IntegerField(),
        ),
    ]
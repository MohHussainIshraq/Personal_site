# Generated by Django 4.1 on 2022-09-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_precent_skill_skill_percent_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=55)),
                ('instagram', models.CharField(max_length=60)),
                ('twiter', models.CharField(max_length=45)),
                ('linkin', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-09-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_portfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_skill', models.CharField(max_length=25)),
                ('precent_skill', models.CharField(max_length=4)),
            ],
        ),
    ]

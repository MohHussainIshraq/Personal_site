# Generated by Django 4.1 on 2022-09-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_portfolio_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('works_completed', models.CharField(max_length=4)),
                ('years_experience', models.CharField(max_length=2)),
                ('total_clients', models.CharField(max_length=4)),
            ],
        ),
    ]

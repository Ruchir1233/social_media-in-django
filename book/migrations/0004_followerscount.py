# Generated by Django 4.1.2 on 2022-10-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]

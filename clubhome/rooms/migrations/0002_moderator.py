# Generated by Django 3.1.7 on 2021-03-19 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_moderator', to='rooms.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_moderator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

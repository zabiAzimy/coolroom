# Generated by Django 4.2.2 on 2023-06-14 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_room_host_topic_message_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='user',
        ),
    ]

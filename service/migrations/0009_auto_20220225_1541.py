# Generated by Django 3.2.7 on 2022-02-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_msg_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='room_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(max_length=20),
        ),
    ]

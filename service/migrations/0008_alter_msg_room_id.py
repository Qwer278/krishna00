# Generated by Django 3.2.7 on 2022-02-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20220225_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='room_id',
            field=models.TextField(max_length=50),
        ),
    ]

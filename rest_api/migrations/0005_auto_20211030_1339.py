# Generated by Django 3.2.4 on 2021-10-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_alter_book_call_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_call',
            name='advisor_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book_call',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
    ]

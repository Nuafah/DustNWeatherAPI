# Generated by Django 4.2.4 on 2024-05-11 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dustnweatherapi', '0004_alter_bangkokdust_table_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangkokweather',
            name='ts',
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-30 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0016_merge_20190831_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_updated',
        ),
    ]

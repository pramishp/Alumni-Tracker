# Generated by Django 2.2.3 on 2019-08-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20190725_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_alumni',
            field=models.BooleanField(default=False, null='False'),
            preserve_default='False',
        ),
    ]

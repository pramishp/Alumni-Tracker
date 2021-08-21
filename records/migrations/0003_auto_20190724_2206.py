# Generated by Django 2.2.3 on 2019-07-24 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20190724_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='be_program',
            field=models.CharField(blank=True, choices=[('BCT', 'BE Computer (BCT)'), ('BEX', 'BE Electronics (BEX)'), ('BEI', 'BEI')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob_bs',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^20[0-9][0-9]/[0-9]{2}/[0-9]{2}$'), django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)]),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivataraccount', '0004_auto_20180508_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmedemail',
            name='digest',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmedopenid',
            name='digest',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]

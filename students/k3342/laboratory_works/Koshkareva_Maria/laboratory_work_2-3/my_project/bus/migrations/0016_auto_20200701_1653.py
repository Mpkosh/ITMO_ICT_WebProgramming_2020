# Generated by Django 3.0.7 on 2020-07-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0015_auto_20200701_1652'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Check',
        ),
        migrations.AddField(
            model_name='schedule',
            name='work_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='work_start',
            field=models.DateTimeField(null=True),
        ),
    ]

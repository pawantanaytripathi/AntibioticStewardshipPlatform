# Generated by Django 3.0.2 on 2020-01-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20200131_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerecord',
            name='in2',
            field=models.CharField(blank=True, default='SOME STRING', max_length=50, null=True),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-03 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_prerecord_resistance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prerecord',
            old_name='immune',
            new_name='immunestatus',
        ),
        migrations.RemoveField(
            model_name='prerecord',
            name='state',
        ),
    ]

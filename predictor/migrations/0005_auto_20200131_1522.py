# Generated by Django 3.0.2 on 2020-01-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0004_auto_20200131_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictor',
            name='infection',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]

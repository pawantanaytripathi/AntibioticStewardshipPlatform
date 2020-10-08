# Generated by Django 3.0.2 on 2020-07-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_remove_approvals_resistance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rcord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antibiotic', models.CharField(blank=True, default='SOME STRING', max_length=50, null=True)),
                ('age', models.CharField(blank=True, default='SOME STRING', max_length=30, null=True)),
                ('infection', models.CharField(blank=True, default='SOME STRING', max_length=50, null=True)),
                ('location', models.CharField(blank=True, default='SOME STRING', max_length=40, null=True)),
                ('gender', models.CharField(blank=True, default='SOME STRING', max_length=20, null=True)),
                ('pregnancy', models.CharField(blank=True, default='SOME STRING', max_length=20, null=True)),
                ('immunestatus', models.CharField(blank=True, default='SOME STRING', max_length=10, null=True)),
            ],
        ),
    ]

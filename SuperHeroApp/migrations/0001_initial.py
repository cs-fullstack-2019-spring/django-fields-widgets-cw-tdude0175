# Generated by Django 2.0.6 on 2019-03-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperHeroModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('HomeLocation', models.CharField(default='', max_length=100)),
                ('RichOrPower', models.CharField(default='', max_length=100)),
                ('Power', models.CharField(default='', max_length=100)),
                ('Alignment', models.CharField(default='', max_length=100)),
                ('PowerUsageExample', models.TextField(default='', max_length=500)),
            ],
        ),
    ]
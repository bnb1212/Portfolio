# Generated by Django 3.0.6 on 2020-06-11 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surveydata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('game_time', models.IntegerField()),
            ],
        ),
    ]

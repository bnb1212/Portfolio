# Generated by Django 3.0.6 on 2020-05-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MySales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sang', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
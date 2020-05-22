# Generated by Django 3.0.6 on 2020-05-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producttab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('stock', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'producttab',
                'managed': False,
            },
        ),
    ]

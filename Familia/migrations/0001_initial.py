# Generated by Django 4.0.4 on 2022-05-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('born', models.DateField()),
                ('rango', models.CharField(max_length=40)),
            ],
        ),
    ]
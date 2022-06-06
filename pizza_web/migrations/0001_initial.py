# Generated by Django 4.0.4 on 2022-06-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('apto_delivery', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='empanada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ingredientes', models.CharField(max_length=60)),
                ('precio', models.FloatField()),
                ('apto_delivery', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ingredientes', models.CharField(max_length=60)),
                ('precio', models.FloatField()),
                ('apto_delivery', models.BooleanField()),
                ('vegana', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='postre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apto_delivery', models.BooleanField()),
                ('gluten_free', models.BooleanField()),
            ],
        ),
    ]
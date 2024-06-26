# Generated by Django 5.0.4 on 2024-05-15 14:34

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Heater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Aquarium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('x', models.FloatField(validators=[django.core.validators.MinValueValidator(10.0)])),
                ('y', models.FloatField(validators=[django.core.validators.MinValueValidator(10.0)])),
                ('z', models.FloatField(validators=[django.core.validators.MinValueValidator(10.0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('filters', models.ManyToManyField(blank=True, to='AquaMaker.filter')),
                ('heater', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='AquaMaker.heater')),
                ('light', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='AquaMaker.light')),
                ('pump', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='AquaMaker.pump')),
            ],
        ),
    ]

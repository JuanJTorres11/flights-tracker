# Generated by Django 4.0 on 2021-12-07 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('stops', models.PositiveSmallIntegerField()),
                ('duration_mins', models.PositiveSmallIntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.airline')),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='arrival_legs', to='api.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departure_legs', to='api.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('price', models.PositiveSmallIntegerField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.agent')),
                ('legs', models.ManyToManyField(to='api.Leg')),
            ],
        ),
    ]

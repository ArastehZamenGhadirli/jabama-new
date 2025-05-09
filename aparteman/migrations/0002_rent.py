# Generated by Django 5.1.6 on 2025-03-21 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparteman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('payment', models.BooleanField()),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aparteman.owner')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aparteman.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aparteman.user')),
            ],
        ),
    ]

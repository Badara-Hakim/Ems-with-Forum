# Generated by Django 3.0.2 on 2020-02-03 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True, help_text='Describe what is special about this room, such as available equipment.', null=True, verbose_name='comment')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('about', models.CharField(blank=True, help_text='See for example the meeting agenda.', max_length=150, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Room', verbose_name='Meeting room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'booking',
                'verbose_name_plural': 'bookings',
            },
        ),
    ]
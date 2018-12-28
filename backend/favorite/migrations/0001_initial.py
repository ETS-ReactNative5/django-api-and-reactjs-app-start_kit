# Generated by Django 2.0.5 on 2018-12-27 21:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('talent', '0002_talent_tid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_time', models.DateTimeField(default=datetime.datetime.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_favorites', to='client.Client')),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talent_favorites', to='talent.Talent')),
            ],
            options={
                'db_table': 'favorite',
                'ordering': ('id', 'client', 'viewed_time', 'talent'),
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('client', 'talent')},
        ),
    ]

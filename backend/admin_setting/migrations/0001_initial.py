# Generated by Django 2.0.2 on 2018-10-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_interview_prep_countdown', models.IntegerField(default=30)),
                ('video_interview_response_time', models.IntegerField(default=120)),
            ],
        ),
    ]

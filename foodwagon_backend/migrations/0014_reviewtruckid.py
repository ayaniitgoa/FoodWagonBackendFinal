# Generated by Django 3.0.6 on 2020-06-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwagon_backend', '0013_reviewchefid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewTruckID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_id', models.IntegerField()),
                ('Name', models.CharField(max_length=200)),
                ('Review', models.CharField(max_length=1024)),
            ],
        ),
    ]

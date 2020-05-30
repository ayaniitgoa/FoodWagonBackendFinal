# Generated by Django 3.0.3 on 2020-05-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Venue_Name', models.CharField(max_length=50)),
                ('Maximum_Guest', models.IntegerField()),
                ('Price_per_Day', models.IntegerField()),
                ('Address', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=50)),
                ('image1', models.ImageField(blank=True, max_length=255, null=True, upload_to='picture/')),
                ('image2', models.ImageField(blank=True, max_length=255, null=True, upload_to='picture/')),
                ('image3', models.ImageField(blank=True, max_length=255, null=True, upload_to='picture/')),
                ('image4', models.ImageField(blank=True, max_length=255, null=True, upload_to='picture/')),
                ('image5', models.ImageField(blank=True, max_length=255, null=True, upload_to='picture/')),
            ],
        ),
    ]
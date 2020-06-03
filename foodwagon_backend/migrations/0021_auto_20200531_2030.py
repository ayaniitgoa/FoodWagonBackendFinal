# Generated by Django 3.0.6 on 2020-05-31 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodwagon_backend', '0020_orderitemchef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemchef',
            name='venue',
        ),
        migrations.AddField(
            model_name='orderitemchef',
            name='chef',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodwagon_backend.Chef'),
        ),
    ]
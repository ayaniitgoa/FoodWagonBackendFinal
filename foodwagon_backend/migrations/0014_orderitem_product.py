# Generated by Django 3.0.6 on 2020-05-31 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodwagon_backend', '0013_auto_20200531_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodwagon_backend.Product'),
        ),
    ]

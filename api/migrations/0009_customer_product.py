# Generated by Django 3.1 on 2020-09-04 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200903_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product'),
        ),
    ]

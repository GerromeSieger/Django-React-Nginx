# Generated by Django 3.1 on 2020-09-05 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200904_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product'),
        ),
    ]

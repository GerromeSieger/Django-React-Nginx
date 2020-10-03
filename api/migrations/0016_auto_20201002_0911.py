# Generated by Django 3.1 on 2020-10-02 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20201002_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='product',
        ),
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product'),
        ),
    ]

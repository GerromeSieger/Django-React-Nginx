# Generated by Django 3.1 on 2020-09-04 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200904_0943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customers',
            new_name='customer',
        ),
    ]

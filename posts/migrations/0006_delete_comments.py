# Generated by Django 3.0.6 on 2020-07-01 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200630_0152'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
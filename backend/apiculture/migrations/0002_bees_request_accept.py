# Generated by Django 4.0.8 on 2023-03-23 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiculture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bees',
            name='request_accept',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-22 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_url', models.CharField(max_length=2083)),
                ('request_method', models.CharField(max_length=6)),
                ('request_body', models.JSONField(blank=True, null=True)),
                ('request_headers', models.JSONField(blank=True, null=True)),
                ('response_code', models.PositiveIntegerField()),
                ('response_content', models.TextField(blank=True, null=True)),
                ('response_elapsed', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

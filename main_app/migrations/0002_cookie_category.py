# Generated by Django 4.2.10 on 2024-02-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='category',
            field=models.CharField(default='traditional', max_length=20),
        ),
    ]
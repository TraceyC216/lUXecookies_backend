# Generated by Django 4.2.10 on 2024-03-02 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cookie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookie',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
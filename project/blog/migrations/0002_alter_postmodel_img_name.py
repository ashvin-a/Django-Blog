# Generated by Django 4.2.7 on 2023-12-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='img_name',
            field=models.ImageField(upload_to='images'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

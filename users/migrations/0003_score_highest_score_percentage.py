# Generated by Django 5.1.7 on 2025-05-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="score",
            name="highest",
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name="score",
            name="percentage",
            field=models.FloatField(default=100.0),
        ),
    ]

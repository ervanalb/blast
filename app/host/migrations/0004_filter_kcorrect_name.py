# Generated by Django 3.2.9 on 2022-06-13 17:54
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("host", "0003_acknowledgement"),
    ]

    operations = [
        migrations.AddField(
            model_name="filter",
            name="kcorrect_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
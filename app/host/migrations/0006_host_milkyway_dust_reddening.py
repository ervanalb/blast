# Generated by Django 3.2.9 on 2022-07-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0005_prospectorresult_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='milkyway_dust_reddening',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

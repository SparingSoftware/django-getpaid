# Generated by Django 3.0.6 on 2020-05-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("getpaid", "0002_auto_20200417_2107"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="redirect_uri",
            field=models.URLField(blank=True, max_length=1024),
        ),
    ]
# Generated by Django 4.1.2 on 2022-12-01 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0005_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="paragraph1",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="paragraph2",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
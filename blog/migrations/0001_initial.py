# Generated by Django 4.1.7 on 2023-02-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=250)),
                ("date", models.DateField(auto_now=True)),
                ("images", models.ImageField(upload_to="blogs/images/")),
            ],
        ),
    ]

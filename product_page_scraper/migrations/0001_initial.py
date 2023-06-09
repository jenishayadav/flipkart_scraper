# Generated by Django 4.1.5 on 2023-01-30 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("url", models.URLField(unique=True, verbose_name="Product URL")),
                ("title", models.CharField(max_length=511)),
                ("brand", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.FloatField()),
                ("mrp", models.FloatField(verbose_name="MRP")),
                ("rating", models.FloatField()),
                ("size", models.CharField(blank=True, max_length=50, null=True)),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                ("image", models.ImageField(upload_to="products/")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="product_page_scraper.product",
                    ),
                ),
            ],
        ),
    ]

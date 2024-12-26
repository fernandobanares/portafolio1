# Generated by Django 4.2.5 on 2024-12-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mensaje",
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
                ("nombre", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("asunto", models.CharField(max_length=150)),
                ("mensaje", models.TextField()),
                ("fecha", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Proyecto",
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
                ("titulo", models.CharField(max_length=200)),
                ("descripcion", models.TextField()),
                ("fecha", models.DateField()),
                (
                    "imagen_principal",
                    models.ImageField(blank=True, null=True, upload_to="proyectos/"),
                ),
                ("url_github", models.URLField(blank=True, null=True)),
                (
                    "herramientas",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("salud", "Salud"),
                            ("comercio", "Comercio"),
                            ("tecnologia", "Tecnología"),
                        ],
                        default="tecnologia",
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]

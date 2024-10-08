# Generated by Django 4.2.16 on 2024-09-23 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QA_ZRE",
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
                ("relation", models.CharField(max_length=255)),
                ("question", models.TextField()),
                ("subject", models.CharField(max_length=255)),
                ("context", models.TextField()),
                ("answers", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Target",
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
                ("target_id", models.CharField(max_length=255)),
                ("target_str", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="RequestedRewrite",
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
                ("prompt", models.TextField()),
                ("relation_id", models.CharField(max_length=255)),
                ("subject", models.CharField(max_length=255)),
                (
                    "target_new",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="new_target",
                        to="dataCollector.target",
                    ),
                ),
                (
                    "target_true",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="true_target",
                        to="dataCollector.target",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Counterfact",
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
                ("case_id", models.IntegerField()),
                ("pararel_idx", models.IntegerField()),
                ("paraphrase_prompts", models.JSONField()),
                ("neighborhood_prompts", models.JSONField()),
                ("attribute_prompts", models.JSONField()),
                ("generation_prompts", models.JSONField()),
                (
                    "requested_rewrite",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dataCollector.requestedrewrite",
                    ),
                ),
            ],
        ),
    ]

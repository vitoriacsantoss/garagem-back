# Generated by Django 5.0.6 on 2024-07-27 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_rename_modelo_veiculo_foto_veiculo"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="veiculo",
            name="imagem",
        ),
        migrations.AddField(
            model_name="veiculo",
            name="modelo",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, related_name="veiculos", to="core.modelo"
            ),
        ),
        migrations.AlterField(
            model_name="veiculo",
            name="foto_veiculo",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
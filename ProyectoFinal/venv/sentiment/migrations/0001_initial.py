# Generated by Django 5.2.2 on 2025-06-12 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('songs', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalisisSentimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_positivo', models.FloatField()),
                ('puntaje_neutro', models.FloatField()),
                ('puntaje_negativo', models.FloatField()),
                ('etiqueta', models.CharField(max_length=50)),
                ('fecha_analisis', models.DateTimeField(auto_now_add=True)),
                ('busqueda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='analisis', to='songs.busquedacancion')),
            ],
            options={
                'verbose_name': 'análisis de sentimiento',
                'verbose_name_plural': 'análisis de sentimientos',
            },
        ),
    ]

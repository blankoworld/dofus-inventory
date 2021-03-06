# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import inventaire.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ressources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_total', models.IntegerField(verbose_name='Total')),
                ('nombre_cachee', models.IntegerField(blank=True, null=True, verbose_name='Quantité cachée')),
                ('date_verifiee', models.DateTimeField(blank=True, null=True)),
                ('date_saisie', models.DateTimeField(default=django.utils.timezone.now)),
                ('dofus_version', models.CharField(default='2.35', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordonnee', models.CharField(max_length=9)),
                ('mapid', models.CharField(blank=True, max_length=10, null=True)),
                ('carte', models.ForeignKey(default=inventaire.models.espace_par_defaut, on_delete=django.db.models.deletion.CASCADE, to='inventaire.Carte')),
            ],
        ),
        migrations.CreateModel(
            name='Origine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('unique_id', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='inventaire',
            name='localisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventaire.Localisation'),
        ),
        migrations.AddField(
            model_name='inventaire',
            name='origine',
            field=models.ForeignKey(default=inventaire.models.origine_par_defaut, on_delete=django.db.models.deletion.CASCADE, to='inventaire.Origine'),
        ),
        migrations.AddField(
            model_name='inventaire',
            name='ressource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ressources.Ressource'),
        ),
    ]

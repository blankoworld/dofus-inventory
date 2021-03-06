# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=120)),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('parente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ressources.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=120)),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('dofus_id', models.CharField(blank=True, max_length=10, verbose_name='ID Dofus')),
                ('categories', models.ManyToManyField(to='ressources.Categorie')),
            ],
        ),
    ]

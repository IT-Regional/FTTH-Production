# Generated by Django 5.0 on 2024-01-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_cluster_n_bandejas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='n_bandejas',
            field=models.IntegerField(choices=[(1, 'numero de bandejas: 1'), (2, 'numero de bandejas: 2'), (3, 'numero de bandejas: 3'), (4, 'numero de bandejas: 4'), (5, 'numero de bandejas: 5'), (6, 'numero de bandejas: 6')], default=1, verbose_name='Numero de Bandejas'),
        ),
    ]

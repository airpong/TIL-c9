# Generated by Django 2.1.5 on 2019-01-31 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exer_190131', '0003_auto_20190131_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-04 21:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_alter_ingredient_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^#?([0-9a-f]{6}|[0-9a-f]{3})$', message='Цвет должен быть указан в Hex формате')], verbose_name='Цвет'),
        ),
    ]

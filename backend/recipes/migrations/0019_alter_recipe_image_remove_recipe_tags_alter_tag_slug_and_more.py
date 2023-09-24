# Generated by Django 4.2.4 on 2023-09-05 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_shoppingcart_recipe_is_favorited_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe', verbose_name='Картинка'),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='tags',
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Слаг'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='recipes.tag', verbose_name='Список тегов'),
        ),
    ]

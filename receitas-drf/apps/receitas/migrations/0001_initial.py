# Generated by Django 5.1.1 on 2024-10-14 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=165)),
                ('slug', models.SlugField()),
                ('preparation_time', models.IntegerField()),
                ('preparation_time_unit', models.CharField(max_length=65)),
                ('servings', models.IntegerField()),
                ('servings_unit', models.CharField(max_length=65)),
                ('preparation_steps', models.TextField()),
                ('preparation_steps_is_html', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='receitas/covers/%Y/%m/%d/')),
            ],
        ),
    ]

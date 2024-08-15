# Generated by Django 5.0.7 on 2024-08-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ingredientes', models.JSONField()),
                ('imagem', models.ImageField(upload_to='receitas/')),
            ],
        ),
    ]

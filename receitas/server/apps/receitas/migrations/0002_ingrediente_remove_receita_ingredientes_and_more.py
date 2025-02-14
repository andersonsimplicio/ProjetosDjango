# Generated by Django 5.0.7 on 2024-08-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='receita',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.ManyToManyField(related_name='receitas', to='receitas.ingrediente'),
        ),
    ]

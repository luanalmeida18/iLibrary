# Generated by Django 4.1.7 on 2023-04-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=50)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Editora',
            },
        ),
    ]

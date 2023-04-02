# Generated by Django 4.1.7 on 2023-04-02 20:31

import cpf_field.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('ra', models.IntegerField(unique=True)),
                ('cpf', cpf_field.models.CPFField(blank=True, error_messages={'invalid': 'CPF inválido'}, max_length=11, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=100)),
                ('bairro', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(blank=True, max_length=50)),
                ('estado', models.CharField(blank=True, max_length=2)),
                ('celular', models.CharField(blank=True, max_length=12)),
                ('email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('sala', models.CharField(blank=True, max_length=10)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Aluno',
            },
        ),
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('edicao', models.IntegerField()),
                ('qtd_disponivel', models.IntegerField()),
                ('isbn', models.CharField(max_length=16, unique=True)),
                ('imagem', models.ImageField(blank=True, upload_to='livros/img/')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.autores')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.categorias')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.editoras')),
            ],
            options={
                'verbose_name': 'Livro',
            },
        ),
    ]

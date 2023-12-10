# Generated by Django 5.0 on 2023-12-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projetosas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id_prof', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('senha', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id_sala', models.AutoField(primary_key=True, serialize=False)),
                ('setor', models.TextField(max_length=255)),
                ('numeracao', models.TextField(max_length=255)),
                ('status', models.TextField(max_length=255)),
                ('horario_disp', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id_solicitacao', models.AutoField(primary_key=True, serialize=False)),
                ('horario', models.TextField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
            ],
        ),
    ]

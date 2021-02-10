# Generated by Django 3.1.5 on 2021-02-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_auto_20210113_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('imagen', models.ImageField(default='null', upload_to='articulos', verbose_name='Miniatura')),
                ('publicado', models.BooleanField(verbose_name='¿Publicado?')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['titulo', 'publicado'],
            },
        ),
        migrations.AlterModelOptions(
            name='articulo',
            options={'ordering': ['titulo', 'publicado'], 'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterField(
            model_name='articulo',
            name='actualizado',
            field=models.DateTimeField(auto_now=True, verbose_name='Editado'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='null', upload_to='articulos', verbose_name='Miniatura'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='publicado',
            field=models.BooleanField(verbose_name='¿Publicado?'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
    ]

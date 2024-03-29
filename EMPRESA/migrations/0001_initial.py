# Generated by Django 2.0 on 2018-10-09 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(help_text='Imagen de 960x650', upload_to='empresa/antecedentes')),
                ('titulo', models.CharField(max_length=100)),
                ('parrafo', models.TextField()),
            ],
            options={
                'verbose_name_plural': '1. Antecedentes',
            },
        ),
        migrations.CreateModel(
            name='BoxItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icono', models.CharField(choices=[('icon-desktop', 'icon-desktop'), ('icon-desktop', 'icon-desktop'), ('icon-desktop', 'icon-desktop')], max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('parrafo', models.TextField()),
            ],
            options={
                'verbose_name_plural': '2. BoxItem',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(help_text='Imagen de 1000x700', upload_to='company/')),
                ('image_2', models.ImageField(help_text='Imagen de 500x730', upload_to='company/')),
                ('image_3', models.ImageField(help_text='Imagen de 500x730', upload_to='company/')),
                ('title_1', models.CharField(max_length=100)),
                ('objetive', models.TextField(blank=True, null=True)),
                ('title_2', models.CharField(blank=True, max_length=100, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('title_3', models.CharField(blank=True, max_length=100, null=True)),
                ('view', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '4. Company',
            },
        ),
        migrations.CreateModel(
            name='CompanyLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='index/Logo')),
                ('logo_with_color', models.ImageField(blank=True, null=True, upload_to='index/Logo')),
                ('logo_white', models.ImageField(blank=True, null=True, upload_to='index/Logo')),
            ],
            options={
                'verbose_name_plural': '7. Company logo',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('street', models.CharField(blank=True, max_length=200, null=True)),
                ('map', models.TextField(blank=True, max_length=800, null=True)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '6. Contact',
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='index/Logo')),
            ],
            options={
                'verbose_name_plural': '5. Provider',
            },
        ),
        migrations.CreateModel(
            name='SeccionFoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_1', models.ImageField(help_text='Imagen de 1000x700', upload_to='empresa/foto_1')),
                ('imagen_2', models.ImageField(help_text='Imagen de 500x730', upload_to='empresa/foto_2')),
                ('titulo_1', models.CharField(max_length=100)),
                ('objetivo', models.TextField(blank=True, null=True)),
                ('titulo_2', models.CharField(blank=True, max_length=100, null=True)),
                ('mision', models.TextField(blank=True, null=True)),
                ('titulo_3', models.CharField(blank=True, max_length=100, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '3. Photos from the home section',
            },
        ),
    ]

# Generated by Django 2.0 on 2018-10-12 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0005_auto_20181011_1406'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visits_Blog',
            new_name='Visitas_Blog',
        ),
        migrations.RenameField(
            model_name='visitas_blog',
            old_name='visit',
            new_name='visita',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image2',
        ),
    ]

# Generated by Django 2.0 on 2018-10-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMPRESA', '0006_auto_20181017_1038'),
    ]

    operations = [
        migrations.DeleteModel(
            name='formulario',
        ),
        migrations.DeleteModel(
            name='FormularioContacto',
        ),
        migrations.AlterField(
            model_name='company',
            name='paragraph_about',
            field=models.TextField(blank=True, max_length=900, null=True),
        ),
    ]

# Generated by Django 2.0 on 2018-10-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRINCIPAL', '0007_auto_20181024_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redessociales',
            name='icono',
            field=models.CharField(choices=[('fab fa-facebook-f', 'facebook'), ('fa fa-user', 'user'), ('fab fa-google-plus-g', 'google-plus'), ('fab fa-instagram', 'instagram')], max_length=100),
        ),
    ]

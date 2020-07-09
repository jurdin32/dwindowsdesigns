# Generated by Django 2.0 on 2018-10-10 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Category',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BLOG.Category_blog'),
        ),
    ]

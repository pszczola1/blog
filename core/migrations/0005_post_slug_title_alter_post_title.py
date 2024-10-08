# Generated by Django 4.1.6 on 2023-03-12 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug_title',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]

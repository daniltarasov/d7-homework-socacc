# Generated by Django 2.2.6 on 2020-06-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200614_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.TextField(),
        ),
    ]

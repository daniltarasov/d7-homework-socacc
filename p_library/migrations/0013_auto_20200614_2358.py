# Generated by Django 2.2.6 on 2020-06-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0012_auto_20200614_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='books',
            field=models.ManyToManyField(blank=True, default=None, to='p_library.Book'),
        ),
    ]

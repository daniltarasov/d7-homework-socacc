# Generated by Django 2.2.6 on 2020-06-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0008_auto_20200614_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('books', models.ManyToManyField(to='p_library.Book')),
            ],
        ),
    ]
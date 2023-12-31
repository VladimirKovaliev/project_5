# Generated by Django 4.2.7 on 2023-12-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'материал',
                'verbose_name_plural': 'материалы',
            },
        ),
        migrations.DeleteModel(
            name='Matrial',
        ),
    ]

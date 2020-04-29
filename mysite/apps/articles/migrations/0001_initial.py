# Generated by Django 3.0.5 on 2020-04-29 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_AD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Назва статті')),
                ('article_text', models.TextField(verbose_name='Текст статті')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
        ),
        migrations.CreateModel(
            name='Article_PG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Назва статті')),
                ('article_text', models.TextField(verbose_name='Текст статті')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_PG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name="Ім'я автора")),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст коментаря')),
                ('comment_pg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article_PG')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_AD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, verbose_name="Ім'я автора")),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст коментаря')),
                ('comment_ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article_AD')),
            ],
        ),
    ]
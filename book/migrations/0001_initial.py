# Generated by Django 2.0.4 on 2018-04-22 16:52

import book.models
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, editable=False, max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, editable=False, max_length=200, null=True)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True, max_length=1000, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Author')),
            ],
            options={
                'ordering': ['title'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, editable=False, null=True)),
                ('name', models.CharField(help_text='Enter a book genre', max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, help_text='Images to be uploaded here will be resized to 1000x300', null=True, upload_to='media//book/')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.PositiveSmallIntegerField()),
                ('alt_title', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('inventory', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(blank=True, help_text='Images to be uploaded here will be resized to 400x600', upload_to=book.models.volume_directory_location)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
            options={
                'ordering': ['title', 'volume'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(to='book.Tag'),
        ),
    ]
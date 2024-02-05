# Generated by Django 3.2.23 on 2024-02-03 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('telephone', models.CharField(max_length=100, null=True)),
                ('joindate', models.DateField()),
                ('popularity_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('joindate', models.DateField()),
                ('popularity_score', models.IntegerField()),
                ('recommendedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orm_practice.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='orm_practice.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='orm_practice.publisher')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='followers',
            field=models.ManyToManyField(related_name='followed_authors', related_query_name='followed_authors', to='orm_practice.User'),
        ),
        migrations.AddField(
            model_name='author',
            name='recommendedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', to='orm_practice.author'),
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-08 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('register_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Talant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='static/images')),
                ('location', models.TextField()),
                ('create_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Solver.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Solver.user')),
            ],
        ),
        migrations.CreateModel(
            name='Aplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('message', models.CharField(max_length=50, null=True)),
                ('duraction', models.TextField()),
                ('create_at', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
                ('talant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Solver.talant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Solver.user')),
            ],
        ),
    ]
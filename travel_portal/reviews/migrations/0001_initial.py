# Generated by Django 4.2.5 on 2023-09-19 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tourpackage')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tourpackage')),
            ],
        ),
    ]

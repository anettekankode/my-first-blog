# Generated by Django 2.1.7 on 2019-02-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_kunde'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Kunde',
        ),
    ]

# Generated by Django 3.0.1 on 2019-12-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/research')),
                ('title', models.CharField(max_length=128)),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
                ('content3', models.TextField()),
            ],
        ),
    ]

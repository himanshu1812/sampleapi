# Generated by Django 2.2.7 on 2020-03-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='student_image')),
                ('college', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]
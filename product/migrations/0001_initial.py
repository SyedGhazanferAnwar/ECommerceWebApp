# Generated by Django 2.1.7 on 2019-03-22 18:10

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('profileImage', models.ImageField(upload_to='')),
                ('Description', models.TextField()),
                ('Discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='singleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'zimageContainer',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='Images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.singleImage'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Category'),
        ),
    ]

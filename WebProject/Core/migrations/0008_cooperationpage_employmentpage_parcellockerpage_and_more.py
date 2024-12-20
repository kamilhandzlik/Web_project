# Generated by Django 5.1.2 on 2024-11-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_serviceterms'),
    ]

    operations = [
        migrations.CreateModel(
            name='CooperationPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description_1_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_1', models.TextField(default='Wstaw akapit.')),
                ('description_2_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_2', models.TextField(default='Wstaw akapit.')),
                ('description_3_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_3', models.TextField(default='Wstaw akapit.')),
                ('description_4_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_4', models.TextField(default='Wstaw akapit.')),
                ('description_5_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_5', models.TextField(default='Wstaw akapit.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description_1_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_1', models.TextField(default='Wstaw akapit.')),
                ('description_2_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_2', models.TextField(default='Wstaw akapit.')),
                ('description_3_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_3', models.TextField(default='Wstaw akapit.')),
                ('description_4_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_4', models.TextField(default='Wstaw akapit.')),
                ('description_5_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_5', models.TextField(default='Wstaw akapit.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParcelLockerPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description_1_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_1', models.TextField(default='Wstaw akapit.')),
                ('description_2_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_2', models.TextField(default='Wstaw akapit.')),
                ('description_3_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_3', models.TextField(default='Wstaw akapit.')),
                ('description_4_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_4', models.TextField(default='Wstaw akapit.')),
                ('description_5_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_5', models.TextField(default='Wstaw akapit.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostPointPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description_1_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_1', models.TextField(default='Wstaw akapit.')),
                ('description_2_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_2', models.TextField(default='Wstaw akapit.')),
                ('description_3_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_3', models.TextField(default='Wstaw akapit.')),
                ('description_4_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_4', models.TextField(default='Wstaw akapit.')),
                ('description_5_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_5', models.TextField(default='Wstaw akapit.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WarehousePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description_1_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_1', models.TextField(default='Wstaw akapit.')),
                ('description_2_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_2', models.TextField(default='Wstaw akapit.')),
                ('description_3_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_3', models.TextField(default='Wstaw akapit.')),
                ('description_4_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_4', models.TextField(default='Wstaw akapit.')),
                ('description_5_subtitle', models.TextField(default='Wstaw tytuł akapitu.')),
                ('description_5', models.TextField(default='Wstaw akapit.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

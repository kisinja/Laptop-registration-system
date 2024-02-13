# Generated by Django 4.1.5 on 2024-02-12 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('specifications', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('contact_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TheftReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(auto_now_add=True)),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('unresolved', 'Unresolved'), ('resolved', 'Resolved')], max_length=20)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.laptop')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('stolen', 'Stolen'), ('recovered', 'Recovered')], default='active', max_length=20)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.laptop')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.student')),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-08 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='IrregularVerbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infinitive', models.CharField(max_length=100)),
                ('preterit', models.CharField(max_length=100)),
                ('past_participle', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=200)),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verbs.letter')),
            ],
        ),
    ]
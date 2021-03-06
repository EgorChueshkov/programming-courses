# Generated by Django 3.1.3 on 2020-12-03 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201129_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toolbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Технология')),
            ],
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='День недели')),
            ],
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_day', models.CharField(max_length=30, verbose_name='Часть дня')),
                ('time_on', models.TimeField(verbose_name='Время начала занятия')),
                ('time_off', models.TimeField(verbose_name='Время конца занятия')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_lecture', to='mainapp.workday', verbose_name='Лекции')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_practice', to='mainapp.workday', verbose_name='Практика')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.worktime', verbose_name='Время занятий')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='timetable',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mainapp.timetable', verbose_name='Расписание'),
        ),
        migrations.AddField(
            model_name='courses',
            name='toolbox_1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='related_toolbox_1', to='mainapp.toolbox', verbose_name='Технология 1'),
        ),
        migrations.AddField(
            model_name='courses',
            name='toolbox_2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='related_toolbox_2', to='mainapp.toolbox', verbose_name='Технология 2'),
        ),
        migrations.AddField(
            model_name='courses',
            name='toolbox_3',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='related_toolbox_3', to='mainapp.toolbox', verbose_name='Технология 3'),
        ),
        migrations.AddField(
            model_name='courses',
            name='toolbox_4',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='related_toolbox_4', to='mainapp.toolbox', verbose_name='Технология 4'),
        ),
    ]

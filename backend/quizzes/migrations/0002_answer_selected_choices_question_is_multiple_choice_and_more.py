# Generated by Django 4.2.7 on 2025-05-18 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='selected_choices',
            field=models.ManyToManyField(blank=True, related_name='selected_in_answers', to='quizzes.choice'),
        ),
        migrations.AddField(
            model_name='question',
            name='is_multiple_choice',
            field=models.BooleanField(default=False, help_text='Whether multiple answers can be selected'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='selected_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.choice'),
        ),
    ]

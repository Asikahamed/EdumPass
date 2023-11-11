# Generated by Django 4.2.6 on 2023-10-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_category_options_quiz'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AddField(
            model_name='lessons',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='lesson_type',
            field=models.CharField(choices=[('article', 'Article'), ('quiz', 'Quiz'), ('video', 'video')], default='article', max_length=20),
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_answer_author_alter_questionlike_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='isRight',
            field=models.BooleanField(default=False),
        ),
    ]

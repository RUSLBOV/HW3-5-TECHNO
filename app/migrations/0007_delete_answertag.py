

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_answer_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerTag',
        ),
    ]



from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_answer_isright'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='tags',
        ),
    ]

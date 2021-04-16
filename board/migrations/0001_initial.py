# Generated by Django 3.2 on 2021-04-16 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        ('fc_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='�젣紐�')),
                ('contents', models.TextField(verbose_name='�궡�슜')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='�벑濡앹떆媛�')),
                ('tags', models.ManyToManyField(to='tag.Tag', verbose_name='�깭洹�')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fc_user.fcuser', verbose_name='�옉�꽦�옄')),
            ],
            options={
                'verbose_name': '패스트캠퍼스 게시글',
                'verbose_name_plural': '패스트캠퍼스 게시글',
                'db_table': 'fastcampus_board',
            },
        ),
    ]
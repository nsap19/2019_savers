# Generated by Django 2.2.3 on 2019-07-19 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='NoticeBoard',
        ),
        migrations.DeleteModel(
            name='Pay',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductColor',
        ),
        migrations.DeleteModel(
            name='ProductLength',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.DeleteModel(
            name='QABoard',
        ),
        migrations.DeleteModel(
            name='QABoardComment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserOrder',
        ),
    ]

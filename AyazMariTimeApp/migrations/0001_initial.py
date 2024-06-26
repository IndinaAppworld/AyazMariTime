# Generated by Django 4.2.11 on 2024-04-18 14:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CURRENCYMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ENGMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FLAGMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GAPMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PAYMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PUMPMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RANKMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SCMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SHIP2Master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VISAMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VSMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VTMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'In Active')], default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DumpData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='NAME')),
                ('rank', models.CharField(blank=True, max_length=50, verbose_name='RANK')),
                ('rank2', models.CharField(blank=True, max_length=50, verbose_name='RANK2')),
                ('customid', models.IntegerField(max_length=10, verbose_name='ID')),
                ('customid2', models.IntegerField(max_length=10, verbose_name='ID2')),
                ('pay1', models.IntegerField(max_length=10, verbose_name='PAY 1')),
                ('exppay', models.IntegerField(max_length=10, verbose_name='EXP PAY')),
                ('alvdate', models.DateField(default=django.utils.timezone.now, verbose_name='AVL DATE')),
                ('onb', models.CharField(blank=True, choices=[('1', 'YES'), ('2', 'NO'), ('3', 'GAP')], max_length=10, verbose_name='ONB')),
                ('mobno', models.BigIntegerField(max_length=15, verbose_name='MOBILE NO')),
                ('dob', models.DateField(verbose_name='DATE OF BIRTH')),
                ('cdc', models.CharField(blank=True, max_length=50, verbose_name='CDC')),
                ('passport', models.CharField(blank=True, max_length=50, unique=True, verbose_name='PASSPORT')),
                ('agn', models.CharField(blank=True, max_length=50, verbose_name='AGN')),
                ('cno', models.CharField(blank=True, max_length=50, verbose_name='CNO')),
                ('comp', models.CharField(blank=True, max_length=50, verbose_name='COMP')),
                ('remarks', models.CharField(blank=True, max_length=50, verbose_name='REMARKS')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.currencymaster', verbose_name='CURRENCY')),
                ('eng', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.engmaster', verbose_name='ENG')),
                ('flag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.flagmaster', verbose_name='FLAG')),
                ('gap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.gapmaster', verbose_name='GAP')),
                ('pay', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.paymaster', verbose_name='PAY')),
                ('pump', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.pumpmaster', verbose_name='PUMP')),
                ('sc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.scmaster', verbose_name='SC')),
                ('ship2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.ship2master', verbose_name='SHIP2')),
                ('visa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.visamaster', verbose_name='VISA')),
                ('vs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.vsmaster', verbose_name='VS')),
                ('vt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AyazMariTimeApp.vtmaster', verbose_name='VT')),
            ],
        ),
    ]

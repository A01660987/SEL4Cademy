# Generated by Django 4.2.6 on 2023-10-10 11:39

import SEL4C.permissions
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=50, unique=True, verbose_name='Competence')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Competence',
                'verbose_name_plural': 'Competences',
                'db_table': 'competence',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('L', 'Licenciatura'), ('M', 'Maestría'), ('D', 'Doctorado')], max_length=1, verbose_name='Tipo')),
                ('name', models.CharField(max_length=100, verbose_name='Título')),
                ('acronym', models.CharField(max_length=10, verbose_name='Siglas')),
            ],
            options={
                'verbose_name': 'Título académico',
                'verbose_name_plural': 'Títulos académicos',
                'ordering': ['institution', 'discipline', 'type'],
            },
        ),
        migrations.CreateModel(
            name='DiagnosisQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(unique=True, verbose_name='Question')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Diagnosis Question',
                'verbose_name_plural': 'Diagnosis Questions',
                'db_table': 'diagnosisquestion',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Disciplina')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Grupo')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Institución')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Institución',
                'verbose_name_plural': 'Instituciones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=25, unique=True, verbose_name='Resource')),
                ('link', models.TextField(unique=True, verbose_name='Link')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre(s)')),
                ('first_lastname', models.CharField(max_length=150, verbose_name='Apellido paterno')),
                ('second_lastname', models.CharField(max_length=150, verbose_name='Apellido materno')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingReagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=50, unique=True, verbose_name='Training Reagent')),
                ('goals', models.TextField(null=True, verbose_name='Goals')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('indications', models.TextField(null=True, verbose_name='Indications')),
                ('questions', models.TextField(null=True, verbose_name='Questions')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('competences', models.ManyToManyField(to='SEL4C.competence')),
                ('resources', models.ManyToManyField(to='SEL4C.resource')),
            ],
            options={
                'verbose_name': 'Training Reagent',
                'verbose_name_plural': 'Training Reagents',
                'db_table': 'trainingreagent',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=25, unique=True, verbose_name='Test')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('diagnosisQuestions', models.ManyToManyField(to='SEL4C.diagnosisquestion')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
                'db_table': 'test',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)], verbose_name='Edad')),
                ('agreed_policies', models.BooleanField(default=True, validators=[SEL4C.permissions.is_agreed_on_policy], verbose_name='¿Acepta las políticas de privacidad?')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No binario'), ('O', 'Otro'), ('P', 'Prefiero no decir')], max_length=1, verbose_name='Género')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='País')),
                ('degree', models.ManyToManyField(to='SEL4C.degree', verbose_name='Título académico')),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.group', verbose_name='Grupo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='ImplementationProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('student', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.student', verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Implementation Process',
                'verbose_name_plural': 'Implementation Processes',
                'db_table': 'implementationprocess',
            },
        ),
        migrations.AddField(
            model_name='degree',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEL4C.discipline', verbose_name='Disciplina'),
        ),
        migrations.AddField(
            model_name='degree',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEL4C.institution', verbose_name='Institución'),
        ),
        migrations.CreateModel(
            name='CompetenceDiagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=True, verbose_name='Completed')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('implementationProcess', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.implementationprocess', verbose_name='Implementation Process')),
            ],
            options={
                'verbose_name': 'Competence Diagnosis',
                'verbose_name_plural': 'Competence Diagnoses',
                'db_table': 'competencediagnosis',
            },
        ),
        migrations.CreateModel(
            name='TrainingActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(editable=False, null=True, verbose_name='Link')),
                ('completed', models.BooleanField(default=True, verbose_name='Completed')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('implementationProcess', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.implementationprocess', verbose_name='Implementation Process')),
                ('trainingReagent', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.trainingreagent', verbose_name='Training Reagent')),
            ],
            options={
                'verbose_name': 'Training Activity',
                'verbose_name_plural': 'Training Activities',
                'db_table': 'trainingactivity',
                'unique_together': {('trainingReagent', 'implementationProcess')},
            },
        ),
        migrations.CreateModel(
            name='DiagnosisTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Answer')),
                ('competenceDiagnosis', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.competencediagnosis', verbose_name='Competence Diagnosis')),
                ('diagnosisQuestion', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.diagnosisquestion', verbose_name='Diagnosis Question')),
            ],
            options={
                'verbose_name': 'Diagnosis Test',
                'verbose_name_plural': 'DiagnosisTests',
                'db_table': 'diagnosistest',
                'unique_together': {('competenceDiagnosis', 'diagnosisQuestion')},
            },
        ),
    ]
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Modules(models.Model):
        AREAS = (
                ('studie', 'studie'),
                ('sociaal', 'sociaal'),
                ('toekomst', 'toekomst'),
                ('studiesociaal', 'studiesociaal'),
                ('studietoekomst', 'studietoekomst'),
                ('sociaaltoekomst', 'sociaaltoekomst')
        )

        TYPES_MODULES = (
                ('Actief', 'Actief'),
                ('Pasief', 'Pasief')
        )

        gebied = models.CharField(max_length=50, choices=AREAS, default='studie')
        naam = models.CharField(max_length=50)
        omschrijving = models.TextField()
        tijd =  models.IntegerField('Tijdsduur', default=0)
        kosten = models.IntegerField('Kosten', default=0)
        baten_vast = models.IntegerField('Vaste baten', default=0)
        baten_flex = models.IntegerField('Flexibele baten', default=0)
        experience_vast = models.IntegerField('Vaste exp', default=0)
        experience_flex = models.IntegerField('Flexibele exp', default=0)
        factor = models.DecimalField(max_digits=3, decimal_places=1, default=0)
        niveau = models.IntegerField('Niveau van course', default=1)
        module_type = models.CharField(max_length=10, choices=TYPES_MODULES, default='Pasief')
        cijfer = models.PositiveIntegerField('Cijfer', default=0 , validators=[MaxValueValidator(100),])

        def __str__(self):
                return self.naam


class Questions(models.Model):
        CHOICES = (
                ('Ja', 'Ja'),
                ('Nee', 'Nee'),
                ('WN', 'Weet niet')
        )

        AREAS = (
                ('studie', 'studie'),
                ('sociaal', 'sociaal'),
                ('toekomst', 'toekomst'),
                ('studiesociaal', 'studiesociaal'),
                ('studietoekomst', 'studietoekomst'),
                ('sociaaltoekomst', 'sociaaltoekomst')
        )

        question = models.TextField()
        answers = models.CharField(max_length=50, choices=CHOICES, default='WN')
        gebied = models.CharField(max_length=50, choices=AREAS, default='studie')
        timestamp = models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.question


class UserProfile(models.Model):
        user = models.OneToOneField(User)

        # additional information
        GENDERS = (
                ('M', 'Man'),
                ('V', 'Vrouw'),
        )
        # General info
        firstname = models.CharField(max_length=50)
        lastname = models.CharField(max_length=50)
        sexe = models.CharField(max_length=1, choices=GENDERS, default='M')
        bank = models.IntegerField('Bank', default=150)
        exp_tot = models.IntegerField('Experience totaal', default=0)
        exp_stud = models.IntegerField('Experience studie', default=0)
        exp_soc = models.IntegerField('Experience sociaal', default=0)
        exp_toek = models.IntegerField('Experience toekomst', default=0)
        niveau = models.IntegerField('Niveau', default=1)

        # Weging voor piechart enzo
        weging_stud = models.IntegerField('Weging studie', default=100, blank=True)
        weging_soc = models.IntegerField('Weging sociaal', default=100, blank=True)
        weging_toek = models.IntegerField('Weging toekomst', default=100, blank=True)

        # relations bitches
        modules = models.ManyToManyField(Modules, blank=True)
        questions = models.ManyToManyField(Questions, blank=True)

        def __str__(self):
                return self.user.username

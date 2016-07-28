from django.db import models
from django.contrib.auth.models import User


class Modules(models.Modules):
        AREAS = (
                ('studie'),
                ('sociaal'),
                ('toekomst'),
                ('studiesociaal'),
                ('studietoekomst'),
                ('sociaaltoekomst')
        )

        gebied = models.CharField(choices=AREAS, default='studie')
        naam = models.CharField(max_length=50)
        omschrijving = models.TextField()
        time = models.IntegerField('Tijdsduur', default=4)
        kosten = models.IntegerField('Kosten', default=100)
        baten_vast = models.IntegerField('Vaste baten', default=100)
        baten_flex = models.IntegerField('Flexibele baten', default=100)
        experience_vast = models.IntegerField('Vaste exp', default=100)
        experience_flex = models.IntegerField('Flexibele exp', default=100)
        factor = models.DecimalField(max_digits=3, decimal_places=1)


class Questions(models.Questions):
        CHOICES = (
                ('Ja', 'Ja'),
                ('Nee', 'Nee'),
                ('WN', 'Weet niet')
        )

        question = models.TextField()
        answers = models.CharField(choices=CHOICES, default='WN')


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

        # Weging voor piechart enzo
        weging_stud = models.IntegerField('Experience studie', default=40)
        weging_soc = models.IntegerField('Experience sociaal', default=30)
        weging_toek = models.IntegerField('Experience toekomst', default=30)

        # relations bitches
        modules = models.ManyToManyField(Modules)
        questions = models.ManyToManyField(Questions)

        def __unicode__(self):
                return self.user.username

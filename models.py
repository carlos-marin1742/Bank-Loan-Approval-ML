from django.db import models

#creating model
class approvals (models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('Yes', 'Yes')
        ('No', 'No')
    )
    GRADUATED_CHOICES = (
        ('Graduated', 'Graduated')
        ('Not Graduated', 'Not Graduated')  
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes')
        ('No', 'No')   
    )
    PROPERTY_CHOICES = (
    ('Rural', 'Rural')
    ('Semiurban', 'Semiurban')
    ('Urban', 'Urban')      
    )

    firstname= models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependants = models.IntegerField()
    applicantincome = models.IntegerField(default = 0)
    coapplicantincome = models.IntegerField(default = 0)
    loanamount = models.IntegerField(default = 0)
    loanterm = models.IntegerField(default = 0)
    credithistory = models.IntegerField(default = 0)
    gender = models.CharField(max_length=15, choice = GENDER_CHOICES)
    married = models.CharField(max_length=15, choice = MARRIED_CHOICES)
    graduationeducation = models.CharField(max_length=15, choice = GRADUATED_CHOICES)
    selfemployed = models.CharField(max_length=15, choice = SELFEMPLOYED_CHOICES)
    area = models.CharField(max_length=15, choice = PROPERTY_CHOICES)

    def __str__(self):
            return '{}, {}'.format(self.lastname, self.firstname)

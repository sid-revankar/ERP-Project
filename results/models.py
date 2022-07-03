from django.db import models
from students.models import Sem1Students, Sem2Students, Sem3Students, Sem4Students, Sem5Students, Sem6Students

# Create your models here

# Model for saving ODD-SEM RESULTS!


class oddSemResult(models.Model):
    reg_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=50, default=None)
    sem = models.IntegerField()
    ex1 = models.CharField(max_length=2, blank=True)
    ex2 = models.CharField(max_length=2, blank=True)
    ex3 = models.CharField(max_length=2, blank=True)
    ex4 = models.CharField(max_length=2, blank=True)
    ex5 = models.CharField(max_length=2, blank=True)
    ex6 = models.CharField(max_length=2, blank=True)
    ex7 = models.CharField(max_length=2, blank=True)
    ex_total = models.IntegerField()
    ia1 = models.CharField(max_length=2, default='')
    ia2 = models.CharField(max_length=2, default='')
    ia3 = models.CharField(max_length=2, default='')
    ia4 = models.CharField(max_length=2, default='')
    ia5 = models.CharField(max_length=2, default='')
    ia6 = models.CharField(max_length=2, default='')
    ia7 = models.CharField(max_length=2, default='')
    ia_total = models.IntegerField()
    total = models.IntegerField(blank=True)
    result = models.CharField(max_length=11)
    kx1 = models.CharField(max_length=5, blank=True)
    ki1 = models.CharField(max_length=2, blank=True)
    k_result = models.CharField(max_length=5)

    def __str__(self):
        return self.student_name


# Model for saving EVEN-SEM RESULTS!
class evenSemResult(models.Model):
    reg_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=50, default=None)
    sem = models.IntegerField()
    ex1 = models.CharField(max_length=2, blank=True)
    ex2 = models.CharField(max_length=2, blank=True)
    ex3 = models.CharField(max_length=2, blank=True)
    ex4 = models.CharField(max_length=2, blank=True)
    ex5 = models.CharField(max_length=2, blank=True)
    ex6 = models.CharField(max_length=2, blank=True)
    ex7 = models.CharField(max_length=2, blank=True)
    ex_total = models.IntegerField()
    ia1 = models.CharField(max_length=2, default='')
    ia2 = models.CharField(max_length=2, default='')
    ia3 = models.CharField(max_length=2, default='')
    ia4 = models.CharField(max_length=2, default='')
    ia5 = models.CharField(max_length=2, default='')
    ia6 = models.CharField(max_length=2, default='')
    ia7 = models.CharField(max_length=2, default='')
    ia_total = models.IntegerField()
    total = models.IntegerField(blank=True)
    result = models.CharField(max_length=11)
    kx1 = models.CharField(max_length=5, blank=True)
    ki1 = models.CharField(max_length=2, blank=True)
    k_result = models.CharField(max_length=5)

    def __str__(self):
        return self.student_name


# IA Choices
IA = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
]

# Model for saving IA-MARKS!


class IaSem1(models.Model):

    class Meta:
        verbose_name_plural = 'IA Sem-1'

    # Actual Model
    ia = models.CharField(
        max_length=1,
        choices=IA,
        default=1,
        )
    rollno = models.ForeignKey(
        Sem1Students, on_delete=models.CASCADE, )
    name = models.CharField(max_length=100, default=None)
    # SUBJECT NAMES
    maths1 = models.IntegerField(default=None)
    foc = models.IntegerField(default=None)
    feee = models.IntegerField(default=None)
    it = models.IntegerField(default=None)
    es = models.IntegerField(default=None)
    # END OF SUBJECT NAMES
    
    total = models.IntegerField(default=None)

    def __str__(self):
        return self.name

# Model for saving IA-MARKS!


class IaSem2(models.Model):

    class Meta:
        verbose_name_plural = 'IA Sem-2'

    # Actual Model
    ia = models.CharField(
        max_length=1,
        choices=IA,
        default=2,
        )
    rollno = models.ForeignKey(
        Sem2Students, on_delete=models.CASCADE, default=None, )
    name = models.CharField(max_length=100, default=None)
    # SUBJECT NAMES
    pms = models.IntegerField(default=None)
    sa = models.IntegerField(default=None)
    ck = models.IntegerField(default=None)
    caeg = models.IntegerField(default=None)
    ma = models.IntegerField(default=None)
    kan = models.IntegerField(default=None)
    # END OF SUBJECT NAMES
    
    total = models.IntegerField(default=None)

    def __str__(self):
        return self.name

# Model for saving IA-MARKS!


class IaSem3(models.Model):

    class Meta:
        verbose_name_plural = 'IA Sem-3'

    # Actual Model
    ia = models.CharField(
        max_length=1,
        choices=IA,
        default=3,
        )
    rollno = models.ForeignKey(
        Sem3Students, on_delete=models.CASCADE, )
    name = models.CharField(max_length=100, default=None)
    # SUBJECT NAMES
    py = models.IntegerField(default=None)
    chma = models.IntegerField(default=None)
    cn = models.IntegerField(default=None)
    dbs = models.IntegerField(default=None)
    kan2 = models.IntegerField(default=None)
    # END OF SUBJECT NAMES
    
    total = models.IntegerField(default=None)

    def __str__(self):
        return self.name

# Model for saving IA-MARKS!


class IaSem4(models.Model):

    class Meta:
        verbose_name_plural = 'IA Sem-4'

    # Actual Model
    ia = models.CharField(
        max_length=1,
        choices=IA,
        default=1,
        )
    rollno = models.ForeignKey(
        Sem4Students, on_delete=models.CASCADE, )
    name = models.CharField(max_length=100, default=None)
    # SUBJECT NAMES
    ds = models.IntegerField(default=None)
    osa = models.IntegerField(default=None)
    java = models.IntegerField(default=None)
    se = models.IntegerField(default=None)
    ic = models.IntegerField(default=None)
    # END OF SUBJECT NAMES
    
    total = models.IntegerField(default=None)

    def __str__(self):
        return self.name

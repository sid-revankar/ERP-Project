from django.db import models
from django.conf import settings
from students.models import *
from django.core.validators import MinValueValidator, MaxValueValidator


class Timetable(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    subject = models.CharField(max_length=70)
    room_no = models.CharField(max_length=7)
    time = models.TimeField()
    semester = models.IntegerField()
    day = models.CharField(max_length=20, default=None)


SEM1_SUBS = (
    ("ENGINEERING MATHEMATICS", "ENGINEERING MATHEMATICS"),

    ("FUNDAMENTALS OF COMPUTER", "FUNDAMENTALS OF COMPUTER"),

    ("FUNDAMENTALS OF ELECTRICAL & ELECTRONICS ENGINEERING LAB",
     "FUNDAMENTALS OF ELECTRICAL & ELECTRONICS ENGINEERING LAB"),

    ("IT SKILLS LAB", "IT SKILLS LAB"),

    ("ENVIRONMENT SUSTAINABILITY", "ENVIRONMENT SUSTAINABILITY"),
)

SEM2_SUBS = (
    ("PROJECT MANAGEMENT SKILLS", "PROJECT MANAGEMENT SKILLS"),

    ("STATISTICS AND ANALYSIS", "STATISTICS AND ANALYSIS"),

    ("COMMUNICATION SKILLS", "COMMUNICATION SKILLS"),

    ("CAEG (COMPUTER AIDED ENGINEERING GRAPHICS)",
     "CAEG (COMPUTER AIDED ENGINEERING GRAPHICS)"),

    ("MULTIMEDIA & ANIMATION", "MULTIMEDIA & ANIMATION"),

    ("KANNADA-1", "KANNADA-1"),
)

SEM3_SUBS = (
    ("PYTHON PROGRAMMING", "PYTHON PROGRAMMING"),

    ("COMPUTER HARDWARE, MAINTENANCE AND ADMINISTRATION",
     "COMPUTER HARDWARE, MAINTENANCE AND ADMINISTRATION"),

    ("COMPUTER NETWORKS", "COMPUTER NETWORKS"),

    ("DATABASE SYSTEM CCONCEPTS & PL/SQL", "DATABASE SYSTEM CCONCEPTS & PL/SQL"),

    ("ಸಾಹಿತ್ಯ ಸಿಂಚನ -II/ ಬಳಕೆ ಕನನಡ-II", "ಸಾಹಿತ್ಯ ಸಿಂಚನ -II/ ಬಳಕೆ ಕನನಡ-II"),
)

SEM4_SUBS = (
    ("DATA STRUCTURES WITH PYTHON", "DATA STRUCTURES WITH PYTHON"),

    ("OPERATING SYSTEM & ADMINISTRATION", "OPERATING SYSTEM & ADMINISTRATION"),

    ("OBJECT ORIENTED PROGRAMMING & DESIGN WITH JAVA",
     "OBJECT ORIENTED PROGRAMMING & DESIGN WITH JAVA"),

    ("Software Engineering principles and practices",
     "Software Engineering principles and practices"),

    ("Indian Constitution", "Indian Constitution"),
)

SEM5_SUBS = (
    ("placeholder", "placeholder"),
)

SEM6_SUBS = (
    ("placeholder", "placeholder"),
)

STATUS = (
    ("Present", "Present"),
    ("Absent", "Absent"),
)


class Sem1Attendance(models.Model):
    roll = models.IntegerField()
    status = models.CharField(max_length=7, choices=STATUS, default="Absent")
    semester = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(1)]
    )
    subject = models.CharField(
        max_length=255, choices=SEM1_SUBS, default=None)
    date = models.DateField()

    def __str__(self):
        return str(self.roll)

    class Meta:
        verbose_name_plural = "Sem-1 Attendance"


class Sem2Attendance(models.Model):
    roll = models.ForeignKey(Sem2Students, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default="Present")
    semester = models.IntegerField(
        default=2, validators=[MinValueValidator(2), MaxValueValidator(2)]
    )
    subject = models.CharField(
        max_length=255, choices=SEM2_SUBS, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sem-2 Attendance"


class Sem3Attendance(models.Model):
    roll = models.ForeignKey(Sem3Students, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default="Present")
    semester = models.IntegerField(
        default=3, validators=[MinValueValidator(3), MaxValueValidator(3)]
    )
    subject = models.CharField(
        max_length=255, choices=SEM3_SUBS, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sem-3 Attendance"


class Sem4Attendance(models.Model):
    roll = models.ForeignKey(Sem4Students, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default="Present")
    semester = models.IntegerField(
        default=4, validators=[MinValueValidator(4), MaxValueValidator(4)]
    )
    subject = models.CharField(
        max_length=255, choices=SEM4_SUBS, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sem-4 Attendance"


class Sem5Attendance(models.Model):
    roll = models.ForeignKey(Sem5Students, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default="Present")
    semester = models.IntegerField(
        default=5, validators=[MinValueValidator(5), MaxValueValidator(5)]
    )
    subject = models.CharField(
        max_length=255, choices=SEM5_SUBS, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sem-5 Attendance"


class Sem6Attendance(models.Model):
    roll = models.ForeignKey(Sem6Students, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default="Present")
    semester = models.IntegerField(
        default=6, validators=[MinValueValidator(6), MaxValueValidator(6)]
    )
    subject = models.CharField(
        max_length=255, choices=SEM6_SUBS, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sem-6 Attendance"

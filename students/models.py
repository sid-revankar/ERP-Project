from django.db import models

# Create your models here.


class Sem1Students(models.Model):
    roll_no = models.IntegerField(default=None)
    ern = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=255)
    contact_no = models.IntegerField(default=None)
    email = models.CharField(max_length=100, default=None)
    class_details = models.CharField(max_length=100, default=None)

    # def __str__(self):
    #     return str(self.roll_no)

    class Meta:
        verbose_name_plural = "Sem-1 Students"


class Sem2Students(models.Model):
    roll_no = models.IntegerField(default=None)
    ern = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=255)
    contact_no = models.IntegerField(default=None)
    email = models.CharField(max_length=100, default=None)
    class_details = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.roll_no)

    class Meta:
        verbose_name_plural = "Sem-2 Students"


class Sem3Students(models.Model):
    roll_no = models.IntegerField(default=None)
    ern = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=255)
    contact_no = models.IntegerField(default=None)
    email = models.CharField(max_length=100, default=None)
    class_details = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.roll_no)

    class Meta:
        verbose_name_plural = "Sem-3 Students"


class Sem4Students(models.Model):
    roll_no = models.IntegerField(default=None)
    ern = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=255)
    contact_no = models.IntegerField(default=None)
    email = models.CharField(max_length=100, default=None)
    class_details = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.roll_no)

    class Meta:
        verbose_name_plural = "Sem-4 Students"


class Sem5Students(models.Model):
    roll_no = models.IntegerField(default=None)
    ern = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=255)
    contact_no = models.IntegerField(default=None)
    email = models.CharField(max_length=100, default=None)
    class_details = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.roll_no)

    class Meta:
        verbose_name_plural = "Sem-5 Students"


class Sem6Students(models.Model):
    roll_no = models.IntegerField(default=None)
    ern = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=255)
    contact_no = models.IntegerField(default=None)
    email = models.CharField(max_length=100, default=None)
    class_details = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.roll_no)

    class Meta:
        verbose_name_plural = "Sem-6 Students"

class feedback(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    reg_no = models.CharField(max_length=10, null=True, blank=True)
    semester = models.CharField(max_length=1, null=True, blank=True)
    about = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

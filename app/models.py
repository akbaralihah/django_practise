from datetime import date

from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"Student(id={self.id}, name={self.first_name}, last_name={self.last_name}, age={self.age})"

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )

    class Meta:
        db_table = "students"


class Course(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "courses"


class StudentCouse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_courses"

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name} - {self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    subject_id = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    teacher_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentPhoto(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='student_photos/')

    def __str__(self):
        return f"Photo for {self.student.name}"

class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'subject')

    def __str__(self):
        return f"{self.teacher.name} -> {self.subject.name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'subject', 'date')

    def __str__(self):
        status = "Present" if self.is_present else "Absent"
        return f"{self.student.name} - {self.subject.name} on {self.date}: {status}"
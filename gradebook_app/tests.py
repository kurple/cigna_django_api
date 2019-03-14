from django.test import TestCase
from .models import Student, Course, Enrollment

# Create your tests here.
class StudentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Student.objects.create(name='Kurt')
        Student.objects.create(name='Peter')

    def test_title_content(self):
        student = Student.objects.get(id=1)
        student2 = Student.objects.get(id=2)
        expected_object_name = f'{student.name}'
        expected_object_name2 = f'{student2.name}'
        self.assertEquals(expected_object_name, 'Kurt')
        self.assertEquals(expected_object_name2, 'Peter')

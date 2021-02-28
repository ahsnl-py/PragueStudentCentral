from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from forum.models import Post, Subject, Department 


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                                          username='testuser'
                                        , password='12345')
        self.department = Department.objects.create(
                                          department_name = "Materials Engineering"
                                        , department_slug = "materials-engineering"
                                        , no_subject = 2 )
        self.subject = Subject.objects.create(
                                          subject_name = "Physics III"
                                        , subject_slug = "physics-iii"
                                        , department_name_id = self.department.id )
        self.post = Post.objects.create(
                                          subject_name_id = 1
                                        , title =  "Create first Unit test"
                                        , author = self.user
                                        , body = "this is by test"
                                        , publish = timezone.now())

    def test_obj_creation(self):
        dept = Department.objects.get(department_name="Materials Engineering")
        subject = Subject.objects.get(subject_name="Physics III")
        post = Post.objects.get(title = "Create first Unit test")
        
        """Test dept model"""
        self.assertTrue(isinstance(dept, Department))
        # self.assertEqual(dept.department_slug, self.department.department_slug)
        self.assertEqual(dept.get_absolute_url(), '/departments/%s/' % (dept.id))

        """Test subject model"""
        self.assertTrue(isinstance(subject, Subject))
        # self.assertEqual(subject.subject_slug, self.subject.subject_slug)
        self.assertEqual(subject.get_absolute_url(), '/departments/%s/%s' % (dept.id, subject.id))

        """Test subject model"""
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.slug, "create-first-unit-test")
        self.assertEqual(post.get_absolute_url(), '/post/%s/%s/' % (post.id, post.slug))
        
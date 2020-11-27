# create folder 'fiels_for_test', add the according files and run the test.
# the section is commented for now in order to be clean


# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.test import TestCase
# from django.core.files.uploadedfile import SimpleUploadedFile
# from Models.models import FaceDetection, UserModel
# from Models.forms import SpamFilterForm, MovieReviewerForm
#
#
# class TestCustomValidators(TestCase):
#
#     def test_type_of_pic_validator_with_valid_should_return(self):
#         fd = FaceDetection(picture= SimpleUploadedFile(name='biker.jpg',
#                                                        content=open('Models/files_for_test/biker.jpg', 'rb').read(),
#                                                        content_type='image/jpeg')
#                            , strength= 1.25)
#         try:
#             fd.full_clean()
#             fd.save()
#         except ValidationError as ex:
#             self.assertIsNone(ex)
#
#     def test_type_of_pic_validator_with_invalid_should_raise(self):
#         fd = FaceDetection(picture=SimpleUploadedFile(name='earth.gif',
#                                                       content=open('Models/files_for_test/earth.gif', 'rb').read(),
#                                                       content_type='image/jpeg'),
#                                                       strength=1.25)
#         try:
#             fd.full_clean()
#             fd.save()
#             self.fail()
#         except ValidationError as ex:
#             self.assertIsNotNone(ex)
#
#     def test_ai_type_validator_with_valid_should_return(self):
#         um = UserModel(jupyter_file= SimpleUploadedFile(name='1.Sentiment Analysis Twitter.ipynb',
#                                                        content=open('Models/files_for_test/1.Sentiment Analysis Twitter.ipynb',
#                                                                     'rb').read()),
#                        pickled_file=SimpleUploadedFile(name='1.linear_svm.pickle',
#                                                        content=open(
#                                                            'Models/files_for_test/linear_svm.pickle',
#                                                            'rb').read(),
#                                                        ),
#                        description='blah-blah',
#                        sender_id=User.objects.create_user('blah', 'blah@gmail.com', 'password').id
#
#                            )
#         try:
#             um.full_clean()
#             um.save()
#         except ValidationError as ex:
#             self.assertIsNone(ex)
#
#     def test_ai_type_validator_with_invalid_should_raise(self):
#         um = UserModel(jupyter_file= SimpleUploadedFile(name='biker.jpg', content=open('Models/files_for_test/1.Sentiment Analysis Twitter.ipynb',
#                                                                                        'rb').read(),),
#                        pickled_file=SimpleUploadedFile(name='Models/files_for_test/1.Sentiment Analysis Twitter.ipynb',
#                                                        content=open(
#                                                            'Models/files_for_test/1.Sentiment Analysis Twitter.ipynb',
#                                                            'rb').read(),
#                                                        ),
#                        description='blah-blah',
#                        sender_id=User.objects.create_user('blah', 'blah@gmail.com', 'password').id)
#         try:
#             um.full_clean()
#             um.save()
#             self.fail()
#         except ValidationError as ex:
#             self.assertIsNotNone(ex)
#
#     def test_notebook_type_validator_with_valid_should_return(self):
#         um = UserModel(jupyter_file= SimpleUploadedFile(name='1.Sentiment Analysis Twitter.ipynb',
#                                                        content=open('Models/files_for_test/1.Sentiment Analysis Twitter.ipynb',
#                                                                     'rb').read()),
#                        pickled_file=SimpleUploadedFile(name='1.linear_svm.pickle',
#                                                        content=open(
#                                                            'Models/files_for_test/linear_svm.pickle',
#                                                            'rb').read(),
#                                                        ),
#                        description='blah-blah',
#                        sender_id=User.objects.create_user('blah', 'blah@gmail.com', 'password').id
#
#                            )
#         try:
#             um.full_clean()
#             um.save()
#         except ValidationError as ex:
#             self.assertIsNone(ex)
#
#     def test_notebook_type_validator_with_invalid_should_raise(self):
#         um = UserModel(jupyter_file= SimpleUploadedFile(name='biker.jpg', content=open('Models/files_for_test/biker.jpg',
#                                                                                        'rb').read(),),
#                        pickled_file=SimpleUploadedFile(name='Models/files_for_test/linear_svm.pickle',
#                                                        content=open(
#                                                            'Models/files_for_test/linear_svm.pickle',
#                                                            'rb').read(),
#                                                        ),
#                        description='blah-blah',
#                        sender_id=User.objects.create_user('blah', 'blah@gmail.com', 'password').id)
#         try:
#             um.full_clean()
#             um.save()
#             self.fail()
#         except ValidationError as ex:
#             self.assertIsNotNone(ex)
#
#     def test_size_validator_with_valid_should_return(self):
#         um = UserModel(jupyter_file= SimpleUploadedFile(name='1.Sentiment Analysis Twitter.ipynb',
#                                                        content=open('Models/files_for_test/1.Sentiment Analysis Twitter.ipynb',
#                                                                     'rb').read()),
#                        pickled_file=SimpleUploadedFile(name='1.linear_svm.pickle',
#                                                        content=open(
#                                                            'Models/files_for_test/linear_svm.pickle',
#                                                            'rb').read(),
#                                                        ),
#                        description='blah-blah',
#                        sender_id=User.objects.create_user('blah', 'blah@gmail.com', 'password').id
#
#                            )
#         try:
#             um.full_clean()
#             um.save()
#         except ValidationError as ex:
#             self.assertIsNone(ex)
#
#     def test_size_validator_with_invalid_should_raise(self):
#         um = UserModel(jupyter_file= SimpleUploadedFile(name='1.Sentiment Analysis Twitter.ipynb',
#                                                         content=open('Models/files_for_test/1.Sentiment Analysis Twitter.ipynb','rb').read(),),
#                        pickled_file=SimpleUploadedFile(name='ensemble.pickle',
#                                                        content=open(
#                                                            'Models/files_for_test/ensemble.pickle',
#                                                            'rb').read(),
#                                                        ),
#                        description='blah-blah',
#                        sender_id=User.objects.create_user('blah', 'blah@gmail.com', 'password').id)
#         try:
#             um.full_clean()
#             um.save()
#             self.fail()
#         except ValidationError as ex:
#             self.assertIsNotNone(ex)
#
#
# class TestForm(TestCase):
#
#     def test_spam_filter_form_with_correct_value_should_be_valid(self):
#         data = {'text': 'dsad123321ssdsadsadsa'}
#         form = SpamFilterForm(data)
#         self.assertTrue(form.is_valid())
#
#     def test_movie_reviewer_form_with_valid_should_be_valid(self):
#         data = {'text': '2131132sadadasdasd'}
#         form = MovieReviewerForm(data)
#         self.assertTrue(form.is_valid())
#

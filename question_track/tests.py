from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_solvedate_greater_than_createdate(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now()
        solvedate_question = Question(solvedate=time)
        self.assertIs(solvedate_question.createdate, solvedate_question)

from django.test import TestCase
from .models import Question, Answer


class QuestionModelTest(TestCase):

    def test_create_question(self):
        q = Question.objects.create(
            text="Mennyi 2 + 2?",
        )
        self.assertEqual(q.text, "Mennyi 2 + 2?")


class AnswerModelTest(TestCase):

    def test_connect_answer_to_question(self):
        q = Question.objects.create(text="Mennyi 3 + 3?")

        a = Answer.objects.create(question=q, text="6", is_correct=True)

        self.assertEqual(a.question, q)
        self.assertTrue(a.is_correct)

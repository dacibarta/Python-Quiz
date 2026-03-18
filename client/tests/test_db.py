import unittest
from client.db import get_questions


class TestDatabaseRead(unittest.TestCase):

    def test_load_questions(self):
        questions = get_questions()
        self.assertIsInstance(questions, list)

import unittest
from unittest.mock import patch, Mock

from resources.student import Student


class TestBigBangResource(unittest.TestCase):

    @patch.object(Student, 'post')
    def test_post_method(self, mock_post):
        mockresponse = Mock(
                    headers={'Content-Type' :'application/json'},
                    status_code=201,
                    json=[
                        "1",
                        "2",
                        "Big",
                        "4",
                        "Bang",
                        "Big",
                        "Theory",
                        "8",
                        "Big",
                        "Bang",
                        "11",
                        "Big",
                        "13",
                        "Theory",
                        "BigBang",
                        "16",
                        "17",
                        "Big",
                        "19",
                        "Bang",
                        "BigTheory"
                    ]
                )
        mock_post.return_value = mockresponse
        student = Student().post()
        expected = [
                        "1",
                        "2",
                        "Big",
                        "4",
                        "Bang",
                        "Big",
                        "Theory",
                        "8",
                        "Big",
                        "Bang",
                        "11",
                        "Big",
                        "13",
                        "Theory",
                        "BigBang",
                        "16",
                        "17",
                        "Big",
                        "19",
                        "Bang",
                        "BigTheory"
                    ]
        self.assertEqual(201, student.status_code)
        self.assertEqual(expected, student.json)


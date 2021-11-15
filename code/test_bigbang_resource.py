import unittest
from unittest.mock import patch, Mock

from code.resources.bigbang import BigBang


class TestBigBangResource(unittest.TestCase):

    @patch.object(BigBang, 'post')
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
        student = BigBang().post()
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


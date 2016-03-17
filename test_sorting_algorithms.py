# Test sorting algorithms

import unittest

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.data = {
            [
                {
                    "name": "Bob",
                    "value": 3
                },
                {
                    "name": "Bobby",
                    "value": 2
                },
                {
                    "name": "Boris",
                    "value": 5
                }
            ]
        }
        self.expected_list = [
            {
                "name": "Bob",
                "value": 3
            },
            {
                "name": "Bobby",
                "value": 2
            },
            {
                "name": "Boris",
                "value": 5
            }
        ]

    def test_insertion_sort(self):
        result_list = insertion(self.data, key="value")
        self.assertEqual(result_list, self.expected_list)

if __name__ == "__main__":
    unittest.main()

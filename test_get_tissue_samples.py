import get_tissue_samples
import unittest


class TestGetGeneCounts(unittest.TestCase):

    def setUp(self):
        self.linear_data = [1, 3, 5, 6, 7]

    def test_linear_search_with_val(self):
        res = get_tissue_samples.linear_search(3, self.linear_data)
        self.assertEqual(res, 1)

    def test_linear_search_without_val(self):
        res = get_tissue_samples.linear_search(0, self.linear_data)
        self.assertEqual(res, -1)

    def test_linear_search_empty_list(self):
        res = get_tissue_samples.linear_search(0, [])
        self.assertEqual(res, -1)


if __name__ == '__main__':
    unittest.main()

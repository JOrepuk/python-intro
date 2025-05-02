import unittest
from pyhelpers.data_utils import flatten_list, unique_elements

class TestDataUtils(unittest.TestCase):

    def test_flatten_list_basic(self):
        """Test flattening nested lists."""
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([[1], [], [2, 3]]), [1, 2, 3])
        self.assertEqual(flatten_list([[], []]), [])

    def test_flatten_list_mixed(self):
        """Test flattening list with non-list elements."""
        self.assertEqual(flatten_list([[1, 2], 3, [4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list(["a", ["b", "c"]]), ["a", "b", "c"])

    def test_flatten_list_invalid(self):
        """Test flatten_list with invalid input."""
        with self.assertRaises(TypeError):
            flatten_list("not a list")
        with self.assertRaises(TypeError):
            flatten_list(123)

    def test_unique_elements_basic(self):
        """Test removing duplicates from list."""
        self.assertEqual(unique_elements([1, 2, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(unique_elements(["a", "b", "a", "c", "b"]), ["a", "b", "c"])
        self.assertEqual(unique_elements([]), [])

    def test_unique_elements_types(self):
        """Test unique_elements with mixed types."""
        self.assertEqual(unique_elements([1, "1", 1]), [1, "1"])

    def test_unique_elements_invalid(self):
        """Test unique_elements with invalid input."""
        with self.assertRaises(TypeError):
            unique_elements("abc")
        with self.assertRaises(TypeError):
            unique_elements(None)
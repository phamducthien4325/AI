import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import unittest
from queues import IndexMinPQ

class TestIndexMinPQ(unittest.TestCase):
    def setUp(self):
        """Thiết lập hàng đợi ưu tiên trước mỗi test."""
        self.pq = IndexMinPQ()
        self.pq.insert('a', 10)
        self.pq.insert('b', 5)
        self.pq.insert('c', 8)

    def test_insert(self):
        """Kiểm tra thêm phần tử vào hàng đợi."""
        self.pq.insert('d', 3)
        self.assertEqual(self.pq.extract_min(), ('d', 3))  # Phần tử nhỏ nhất phải là ('d', 3)

    def test_extract_min(self):
        """Kiểm tra trích xuất phần tử nhỏ nhất."""
        self.assertEqual(self.pq.extract_min(), ('b', 5))  # ('b', 5) nhỏ nhất
        self.assertEqual(self.pq.extract_min(), ('c', 8))  # Tiếp theo là ('c', 8)

    def test_decrease_key(self):
        """Kiểm tra giảm giá trị ưu tiên."""
        self.pq.decrease_key('c', 4)
        self.assertEqual(self.pq.extract_min(), ('c', 4))  # Giảm xuống còn 4 nên phải ra trước

    def test_increase_key(self):
        """Kiểm tra tăng giá trị ưu tiên."""
        self.pq.increase_key('b', 15)
        self.assertEqual(self.pq.extract_min(), ('c', 8))  # ('c', 8) nhỏ nhất

    def test_delete(self):
        """Kiểm tra xóa phần tử."""
        self.pq.delete('b')  # Xóa 'b' (giá trị 5)
        self.assertNotIn('b', self.pq.position)
        self.assertEqual(self.pq.extract_min(), ('c', 8))  # ('c', 8) nhỏ nhất sau khi xóa

    def test_contains(self):
        """Kiểm tra contains() hoạt động đúng."""
        self.assertTrue(self.pq.contains('a'))
        self.assertFalse(self.pq.contains('z'))

    def test_is_empty(self):
        """Kiểm tra hàng đợi có rỗng không."""
        self.assertFalse(self.pq.is_empty())
        self.pq.extract_min()
        self.pq.extract_min()
        self.pq.extract_min()
        self.assertTrue(self.pq.is_empty())

    def test_error_on_duplicate_insert(self):
        """Kiểm tra lỗi khi chèn key đã tồn tại."""
        with self.assertRaises(KeyError):
            self.pq.insert('a', 20)  # Key 'a' đã tồn tại

    def test_error_on_extract_empty(self):
        """Kiểm tra lỗi khi trích xuất từ hàng đợi rỗng."""
        self.pq.extract_min()
        self.pq.extract_min()
        self.pq.extract_min()
        with self.assertRaises(IndexError):
            self.pq.extract_min()

    def test_error_on_invalid_decrease(self):
        """Kiểm tra lỗi khi decrease_key với giá trị lớn hơn hiện tại."""
        with self.assertRaises(ValueError):
            self.pq.decrease_key('c', 20)

    def test_error_on_invalid_increase(self):
        """Kiểm tra lỗi khi increase_key với giá trị nhỏ hơn hiện tại."""
        with self.assertRaises(ValueError):
            self.pq.increase_key('c', 2)

if __name__ == '__main__':
    unittest.main()

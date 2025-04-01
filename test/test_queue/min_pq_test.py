import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import unittest
from queues.min_pq import MinPQ

class TestMinPQ(unittest.TestCase):
    def setUp(self):
        """Chạy trước mỗi test case"""
        self.pq = MinPQ()

    def test_is_empty_initial(self):
        """Kiểm tra ban đầu hàng đợi có rỗng không"""
        self.assertTrue(self.pq.is_empty())

    def test_insert_and_del_min(self):
        """Kiểm tra chèn và xóa phần tử nhỏ nhất"""
        self.pq.insert(5)
        self.pq.insert(10)
        self.pq.insert(3)
        self.pq.insert(8)

        self.assertEqual(self.pq.del_min(), 3)  # 3 nhỏ nhất
        self.assertEqual(self.pq.del_min(), 5)  # 5 là nhỏ nhất còn lại
        self.assertEqual(self.pq.del_min(), 8)  # Tiếp theo là 8
        self.assertEqual(self.pq.del_min(), 10) # Cuối cùng là 10
        self.assertTrue(self.pq.is_empty())      # Hàng đợi phải rỗng

    def test_insert_duplicate_values(self):
        """Kiểm tra khi chèn các giá trị trùng lặp"""
        self.pq.insert(7)
        self.pq.insert(7)
        self.pq.insert(7)

        self.assertEqual(self.pq.del_min(), 7)
        self.assertEqual(self.pq.del_min(), 7)
        self.assertEqual(self.pq.del_min(), 7)
        self.assertTrue(self.pq.is_empty())

    def test_mixed_insert_and_del_min(self):
        """Kiểm tra thêm và xóa xen kẽ"""
        self.pq.insert(15)
        self.pq.insert(20)
        self.assertEqual(self.pq.del_min(), 15)

        self.pq.insert(5)
        self.pq.insert(30)
        self.assertEqual(self.pq.del_min(), 5)

        self.pq.insert(25)
        self.assertEqual(self.pq.del_min(), 20)
        self.assertEqual(self.pq.del_min(), 25)
        self.assertEqual(self.pq.del_min(), 30)
        self.assertTrue(self.pq.is_empty())

if __name__ == '__main__':
    unittest.main()
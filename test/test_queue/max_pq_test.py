import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import unittest
from queues import MaxPQ

class TestMaxPQ(unittest.TestCase):
    def setUp(self):
        """Chạy trước mỗi test case"""
        self.pq = MaxPQ()

    def test_is_empty_initial(self):
        """Kiểm tra ban đầu hàng đợi có rỗng không"""
        self.assertTrue(self.pq.is_empty())

    def test_insert_and_del_max(self):
        """Kiểm tra chèn và xóa phần tử lớn nhất"""
        self.pq.insert(5)
        self.pq.insert(10)
        self.pq.insert(3)
        self.pq.insert(8)

        self.assertEqual(self.pq.del_max(), 10)  # 10 lớn nhất
        self.assertEqual(self.pq.del_max(), 8)   # 8 là lớn nhất còn lại
        self.assertEqual(self.pq.del_max(), 5)   # Tiếp theo là 5
        self.assertEqual(self.pq.del_max(), 3)   # Cuối cùng là 3
        self.assertTrue(self.pq.is_empty())      # Hàng đợi phải rỗng

    def test_insert_duplicate_values(self):
        """Kiểm tra khi chèn các giá trị trùng lặp"""
        self.pq.insert(7)
        self.pq.insert(7)
        self.pq.insert(7)

        self.assertEqual(self.pq.del_max(), 7)
        self.assertEqual(self.pq.del_max(), 7)
        self.assertEqual(self.pq.del_max(), 7)
        self.assertTrue(self.pq.is_empty())

    def test_mixed_insert_and_del_max(self):
        """Kiểm tra thêm và xóa xen kẽ"""
        self.pq.insert(15)
        self.pq.insert(20)
        self.assertEqual(self.pq.del_max(), 20)

        self.pq.insert(5)
        self.pq.insert(30)
        self.assertEqual(self.pq.del_max(), 30)

        self.pq.insert(25)
        self.assertEqual(self.pq.del_max(), 25)
        self.assertEqual(self.pq.del_max(), 15)
        self.assertEqual(self.pq.del_max(), 5)
        self.assertTrue(self.pq.is_empty())

if __name__ == '__main__':
    unittest.main()

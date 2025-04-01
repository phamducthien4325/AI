class IndexMinPQ:
    def __init__(self):
        self.heap = []  # (value, index) pairs
        self.position = {}  # index -> position in heap

    def _swap(self, i, j):
        """Hoán đổi hai phần tử trong heap và cập nhật vị trí trong từ điển."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i][1]] = i
        self.position[self.heap[j][1]] = j

    def _heapify_up(self, i):
        """Đưa phần tử ở vị trí i lên đúng vị trí trong heap."""
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:  # So sánh giá trị
                self._swap(i, parent)
                i = parent
            else:
                break

    def _heapify_down(self, i):
        """Đưa phần tử ở vị trí i xuống đúng vị trí trong heap."""
        size = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def insert(self, index, value):
        """Thêm một phần tử vào hàng đợi ưu tiên."""
        if index in self.position:
            raise KeyError("Index already exists in the queue")
        self.heap.append((value, index))
        self.position[index] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Lấy và xóa phần tử có giá trị nhỏ nhất."""
        if not self.heap:
            raise IndexError("Priority queue is empty")
        min_value, min_index = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        del self.position[min_index]
        self._heapify_down(0)
        return min_index, min_value

    def decrease_key(self, index, new_value):
        """Giảm giá trị của phần tử theo chỉ mục."""
        if index not in self.position:
            raise KeyError("Index not found")
        i = self.position[index]
        if new_value >= self.heap[i][0]:
            raise ValueError("New value must be smaller than current value")
        self.heap[i] = (new_value, index)
        self._heapify_up(i)

    def increase_key(self, index, new_value):
        """Tăng giá trị của phần tử theo chỉ mục."""
        if index not in self.position:
            raise KeyError("Index not found")
        i = self.position[index]
        if new_value <= self.heap[i][0]:
            raise ValueError("New value must be greater than current value")
        self.heap[i] = (new_value, index)
        self._heapify_down(i)

    def delete(self, index):
        """Xóa phần tử theo chỉ mục."""
        if index not in self.position:
            raise KeyError("Index not found")
        i = self.position[index]
        self._swap(i, len(self.heap) - 1)
        self.heap.pop()
        del self.position[index]
        if i < len(self.heap):
            # Chỉ cần heapify theo một hướng
            if i > 0 and self.heap[i][0] < self.heap[(i - 1) // 2][0]:
                self._heapify_up(i)
            else:
                self._heapify_down(i)

    def contains(self, index):
        """Kiểm tra xem chỉ mục có trong hàng đợi không."""
        return index in self.position

    def is_empty(self):
        """Kiểm tra xem hàng đợi có rỗng không."""
        return not self.heap
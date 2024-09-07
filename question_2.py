from collections import deque


class CircularBufferList:
    """Использование стандартного списка Python"""

    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.start = 0
        self.end = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            raise BufferError("Buffer is full")
        self.buffer[self.end] = value
        self.end = (self.end + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise BufferError("Buffer is empty")
        value = self.buffer[self.start]
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return value


"Плюсы: реализация контролируется вручную."
"Минусы: требует больше кода для обработки индексов."


class CircularBufferDeque:
    """Использование collections.deque"""

    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def enqueue(self, value):
        if len(self.buffer) == self.buffer.maxlen:
            raise BufferError("Buffer is full")
        self.buffer.append(value)

    def dequeue(self):
        if len(self.buffer) == 0:
            raise BufferError("Buffer is empty")
        return self.buffer.popleft()


"Плюсы: минимальный код. Поддерживает добавление и удаление элементов."
"Минусы: ограниченные возможности кастомизации."

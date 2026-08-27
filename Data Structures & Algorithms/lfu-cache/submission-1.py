class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value

        self.bucket: "LinkedList | None" = None
        self.prev: Node | None = None
        self.next: Node | None = None


class LinkedList:
    def __init__(self, frequency: int) -> None:
        self.frequency = frequency

        self.sentinel = Node(0, 0)
        self.sentinel.bucket = self
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def is_empty(self) -> bool:
        return self.sentinel.next is self.sentinel

    def append(self, node: Node) -> None:
        assert node.bucket is None

        first = self.sentinel.next
        assert first is not None

        node.bucket = self
        node.prev = self.sentinel
        node.next = first

        first.prev = node
        self.sentinel.next = node

    def remove(self, node: Node) -> None:
        assert node.bucket is self

        previous = node.prev
        following = node.next

        assert previous is not None
        assert following is not None

        previous.next = following
        following.prev = previous

        node.bucket = None
        node.prev = None
        node.next = None

    def pop(self) -> Node:
        last = self.sentinel.prev
        assert last is not None and last is not self.sentinel

        self.remove(last)

        return last


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0

        self.nodes: dict[int, Node] = {}

        self.minimum: LinkedList | None = None
        self.frequencies: dict[int, LinkedList] = {}

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1

        self.promote(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)

        if node is not None:
            node.value = value
            self.promote(node)
            return

        if self.size == self.capacity:
            minimum = self.minimum
            assert minimum is not None

            removed = minimum.pop()
            del self.nodes[removed.key]

            if minimum.is_empty() and minimum.frequency != 1:
                del self.frequencies[minimum.frequency]

        else:
            self.size += 1

        node = Node(key, value)
        self.nodes[key] = node

        bucket = self.get_or_create_bucket(1)
        bucket.append(node)

        self.minimum = bucket

    def promote(self, node: Node) -> None:
        current = node.bucket
        assert current is not None

        bucket = self.get_or_create_bucket(current.frequency + 1)
        current.remove(node)

        if current.is_empty():
            del self.frequencies[current.frequency]

            if current is self.minimum:
                self.minimum = bucket

        bucket.append(node)

    def get_or_create_bucket(self, frequency: int) -> LinkedList:
        bucket = self.frequencies.get(frequency)

        if bucket is None:
            bucket = LinkedList(frequency)
            self.frequencies[frequency] = bucket

        return bucket


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

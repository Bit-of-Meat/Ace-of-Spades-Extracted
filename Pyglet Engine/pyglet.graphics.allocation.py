# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.graphics.allocation
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

class AllocatorMemoryException(Exception):

    def __init__(self, requested_capacity):
        self.requested_capacity = requested_capacity


class Allocator(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.starts = []
        self.sizes = []

    def set_capacity(self, size):
        self.capacity = size

    def alloc(self, size):
        if size == 0:
            return 0
        if not self.starts:
            if size <= self.capacity:
                self.starts.append(0)
                self.sizes.append(size)
                return 0
            raise AllocatorMemoryException(size)
        free_start = self.starts[0] + self.sizes[0]
        for i, (alloc_start, alloc_size) in enumerate(zip(self.starts[1:], self.sizes[1:])):
            free_size = alloc_start - free_start
            if free_size == size:
                self.sizes[i] += free_size + alloc_size
                del self.starts[i + 1]
                del self.sizes[i + 1]
                return free_start
            if free_size > size:
                self.sizes[i] += size
                return free_start
            free_start = alloc_start + alloc_size

        free_size = self.capacity - free_start
        if free_size >= size:
            self.sizes[-1] += size
            return free_start
        raise AllocatorMemoryException(self.capacity + size - free_size)

    def realloc(self, start, size, new_size):
        if new_size == 0:
            if size != 0:
                self.dealloc(start, size)
            return 0
        if size == 0:
            return self.alloc(new_size)
        if new_size < size:
            self.dealloc(start + new_size, size - new_size)
            return start
        for i, (alloc_start, alloc_size) in enumerate(zip(*(self.starts, self.sizes))):
            p = start - alloc_start
            if p >= 0 and size <= alloc_size - p:
                break

        if not (p >= 0 and size <= alloc_size - p):
            print zip(self.starts, self.sizes)
            print start, size, new_size
            print p, alloc_start, alloc_size
        if size == alloc_size - p:
            is_final_block = i == len(self.starts) - 1
            if not is_final_block:
                free_size = self.starts[i + 1] - (start + size)
            else:
                free_size = self.capacity - (start + size)
            if free_size == new_size - size and not is_final_block:
                self.sizes[i] += free_size + self.sizes[i + 1]
                del self.starts[i + 1]
                del self.sizes[i + 1]
                return start
            if free_size > new_size - size:
                self.sizes[i] += new_size - size
                return start
        result = self.alloc(new_size)
        self.dealloc(start, size)
        return result

    def dealloc(self, start, size):
        if size == 0:
            return
        for i, (alloc_start, alloc_size) in enumerate(zip(*(self.starts, self.sizes))):
            p = start - alloc_start
            if p >= 0 and size <= alloc_size - p:
                break

        if p == 0 and size == alloc_size:
            del self.starts[i]
            del self.sizes[i]
        elif p == 0:
            self.starts[i] += size
            self.sizes[i] -= size
        elif size == alloc_size - p:
            self.sizes[i] -= size
        else:
            self.sizes[i] = p
            self.starts.insert(i + 1, start + size)
            self.sizes.insert(i + 1, alloc_size - (p + size))

    def get_allocated_regions(self):
        return (
         self.starts, self.sizes)

    def get_fragmented_free_size(self):
        if not self.starts:
            return 0
        total_free = 0
        free_start = self.starts[0] + self.sizes[0]
        for i, (alloc_start, alloc_size) in enumerate(zip(self.starts[1:], self.sizes[1:])):
            total_free += alloc_start - free_start
            free_start = alloc_start + alloc_size

        return total_free

    def get_free_size(self):
        if not self.starts:
            return self.capacity
        free_end = self.capacity - (self.starts[-1] + self.sizes[-1])
        return self.get_fragmented_free_size() + free_end

    def get_usage(self):
        return 1.0 - self.get_free_size() / float(self.capacity)

    def get_fragmentation(self):
        free_size = self.get_free_size()
        if free_size == 0:
            return 0.0
        return self.get_fragmented_free_size() / float(self.get_free_size())

    def _is_empty(self):
        return not self.starts

    def __str__(self):
        return 'allocs=' + repr(zip(self.starts, self.sizes))

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, str(self))
# okay decompiling out\pyglet.graphics.allocation.pyc

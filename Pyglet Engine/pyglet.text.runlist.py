# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text.runlist
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

class _Run(object):

    def __init__(self, value, count):
        self.value = value
        self.count = count

    def __repr__(self):
        return 'Run(%r, %d)' % (self.value, self.count)


class RunList(object):

    def __init__(self, size, initial):
        self.runs = [
         _Run(initial, size)]

    def insert(self, pos, length):
        i = 0
        for run in self.runs:
            if i <= pos <= i + run.count:
                run.count += length
            i += run.count

    def delete(self, start, end):
        i = 0
        for run in self.runs:
            if end - start == 0:
                break
            if i <= start <= i + run.count:
                trim = min(end - start, i + run.count - start)
                run.count -= trim
                end -= trim
            i += run.count

        self.runs = [ r for r in self.runs if r.count > 0 ]
        if not self.runs:
            self.runs = [
             _Run(run.value, 0)]

    def set_run(self, start, end, value):
        if end - start <= 0:
            return
        else:
            i = 0
            start_i = None
            start_trim = 0
            end_i = None
            end_trim = 0
            for run_i, run in enumerate(self.runs):
                count = run.count
                if i < start < i + count:
                    start_i = run_i
                    start_trim = start - i
                if i < end < i + count:
                    end_i = run_i
                    end_trim = end - i
                i += count

            if start_i is not None:
                run = self.runs[start_i]
                self.runs.insert(start_i, _Run(run.value, start_trim))
                run.count -= start_trim
                if end_i is not None:
                    if end_i == start_i:
                        end_trim -= start_trim
                    end_i += 1
            if end_i is not None:
                run = self.runs[end_i]
                self.runs.insert(end_i, _Run(run.value, end_trim))
                run.count -= end_trim
            i = 0
            for run in self.runs:
                if start <= i and i + run.count <= end:
                    run.value = value
                i += run.count

            last_run = self.runs[0]
            for run in self.runs[1:]:
                if run.value == last_run.value:
                    run.count += last_run.count
                    last_run.count = 0
                last_run = run

            self.runs = [ r for r in self.runs if r.count > 0 ]
            return

    def __iter__(self):
        i = 0
        for run in self.runs:
            yield (
             i, i + run.count, run.value)
            i += run.count

    def get_run_iterator(self):
        return RunIterator(self)

    def __getitem__(self, index):
        i = 0
        for run in self.runs:
            if i <= index < i + run.count:
                return run.value
            i += run.count

        if index == i:
            return self.runs[-1].value

    def __repr__(self):
        return str(list(self))


class AbstractRunIterator(object):

    def __getitem__(self, index):
        pass

    def ranges(self, start, end):
        pass


class RunIterator(AbstractRunIterator):

    def __init__(self, run_list):
        self._run_list_iter = iter(run_list)
        self.start, self.end, self.value = self.next()

    def next(self):
        return self._run_list_iter.next()

    def __getitem__(self, index):
        while index >= self.end and index > self.start:
            self.start, self.end, self.value = self.next()

        return self.value

    def ranges(self, start, end):
        while start >= self.end:
            self.start, self.end, self.value = self.next()

        yield (
         start, min(self.end, end), self.value)
        while end > self.end:
            self.start, self.end, self.value = self.next()
            yield (self.start, min(self.end, end), self.value)


class OverriddenRunIterator(AbstractRunIterator):

    def __init__(self, base_iterator, start, end, value):
        self.iter = base_iterator
        self.override_start = start
        self.override_end = end
        self.override_value = value

    def ranges(self, start, end):
        if end <= self.override_start or start >= self.override_end:
            for r in self.iter.ranges(start, end):
                yield r

        else:
            if start < self.override_start < end:
                for r in self.iter.ranges(start, self.override_start):
                    yield r

            yield (
             max(self.override_start, start),
             min(self.override_end, end),
             self.override_value)
            if start < self.override_end < end:
                for r in self.iter.ranges(self.override_end, end):
                    yield r

    def __getitem__(self, index):
        if self.override_start <= index < self.override_end:
            return self.override_value
        else:
            return self.iter[index]


class FilteredRunIterator(AbstractRunIterator):

    def __init__(self, base_iterator, filter, default):
        self.iter = base_iterator
        self.filter = filter
        self.default = default

    def ranges(self, start, end):
        for start, end, value in self.iter.ranges(start, end):
            if self.filter(value):
                yield (
                 start, end, value)
            else:
                yield (
                 start, end, self.default)

    def __getitem__(self, index):
        value = self.iter[index]
        if self.filter(value):
            return value
        return self.default


class ZipRunIterator(AbstractRunIterator):

    def __init__(self, range_iterators):
        self.range_iterators = range_iterators

    def ranges(self, start, end):
        iterators = [ i.ranges(start, end) for i in self.range_iterators ]
        starts, ends, values = zip(*[ i.next() for i in iterators ])
        starts = list(starts)
        ends = list(ends)
        values = list(values)
        while start < end:
            min_end = min(ends)
            yield (start, min_end, values)
            start = min_end
            for i, iterator in enumerate(iterators):
                if ends[i] == min_end:
                    starts[i], ends[i], values[i] = iterator.next()

    def __getitem__(self, index):
        return [ i[index] for i in self.range_iterators ]


class ConstRunIterator(AbstractRunIterator):

    def __init__(self, length, value):
        self.length = length
        self.value = value

    def next(self):
        yield (
         0, self.length, self.value)

    def ranges(self, start, end):
        yield (
         start, end, self.value)

    def __getitem__(self, index):
        return self.value
# okay decompiling out\pyglet.text.runlist.pyc

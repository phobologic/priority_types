from collections import MutableMapping, OrderedDict, MutableSet


class PriorityMapping(MutableMapping):
    def __init__(self):
        self._store = OrderedDict()
        self._count = OrderedDict()

    def __getitem__(self, key):
        return self._store.__getitem__(key)

    def __setitem__(self, key, value):
        self._count[key] = self._count.setdefault(key, 0) + 1
        return self._store.__setitem__(key, value)

    def __delitem__(self, key):
        self._store.__delitem__(key)
        self._count.__delitem__(key)

    def __iter__(self):
        sorter = self._count.items()
        sorter.sort(key=lambda i: i[1], reverse=True)
        return [x[0] for x in sorter].__iter__()

    def __len__(self):
        return self._store.__len__()


class PrioritySet(MutableSet):
    """ A MutableSet that orders items based first on the number of times
    they are added, and then by add order after that.

    >>> s = PrioritySet()
    >>>
    >>> s.add('a')
    >>> s.add('b')
    >>> s.add('c')
    >>> list(s)
    ['a', 'b', 'c']
    >>> s.add('c')
    >>> list(s)
    ['c', 'a', 'b']
    """
    def __init__(self):
        self._store = OrderedDict()

    def __contains__(self, item):
        return self._store.__contains__(item)

    def __iter__(self):
        sorter = self._store.items()
        sorter.sort(key=lambda i: i[1], reverse=True)
        return [x[0] for x in sorter].__iter__()

    def __len__(self):
        return self._store.__len__()

    def add(self, value):
        self._store[value] = self._store.setdefault(value, 0) + 1

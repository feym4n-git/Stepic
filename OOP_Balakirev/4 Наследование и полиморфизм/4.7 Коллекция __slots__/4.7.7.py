class Note:
    __slots__ = ('_name', '_ton')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            if value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
                raise ValueError('недопустимое значение аргумента')
            super().__setattr__('_name', value)
        elif key == '_ton':
            if value not in (-1, 0, 1):
                raise ValueError('недопустимое значение аргумента')
            super().__setattr__('_ton', value)


class Notes:
    __instanse = None

    def __new__(cls):
        if cls.__instanse is None:
            cls.__instanse = object.__new__(cls)
        return cls.__instanse

    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __getitem__(self, key):
        if 6 < key < 0:
            raise IndexError('недопустимый индекс')
        lst = [self._do, self._re, self._mi, self._fa, self._solt, self._la, self._si]
        return lst[key]
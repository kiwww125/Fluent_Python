import collections


class StrKeyDict(collections.UserDict):
    # we have instance variable 'data' inherited from UserDict, which is Dict object.
    # check __init__ from UserDict

    def __missing__(self, key):
        if not isinstance(key, str):
            return KeyError(key)
        return self.data[str(key)]

    def __contains__(self, key):
        return key in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

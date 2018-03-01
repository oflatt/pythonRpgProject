from variables import devmode
class FrozenClass(object):
    __isfrozen = False
    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError("%r is from a frozen class" % self + " so new attribute " + str(key) + " cannot be set")
        object.__setattr__(self, key, value)

    def _freeze(self):
        if devmode: # only freeze the class for dev mode
            self.__isfrozen = True

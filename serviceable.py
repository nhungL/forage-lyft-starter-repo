from abc import ABCMeta, abstractmethod
"""@Interface"""


class Serviceable(ABCMeta):
    __metaclass__ = ABCMeta
    @abstractmethod
    def needs_service(self):
        pass
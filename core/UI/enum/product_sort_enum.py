from enum import Enum



class ProductSortEnum(Enum):

    HIGH_2_LOW = 'hilo'
    LOW_2_HIGH = 'lohi'
    NAME_A_Z = 'az'
    NAME_Z_A = 'za'

    @classmethod
    def default_value(cls):
        return cls.NAME_A_Z.value


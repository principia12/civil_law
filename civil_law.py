from legal_ontology import LegalEntity, LegalRight
from legal_statements import *

class 인(LegalEntity):
    """민법 2장에서 정의하는 인.
    """
    def __init__(self, 권리들, 의무들, 소유물들, 주소):
        for 권리 in 권리들:
            assert issubclass(type(권리), LegalRight)
        self.근거조항 = 민법_제3조
        self.권리들 = 권리들

class 물건(LegalEntity):
    """
    """
    def __init__(self, 동산여부, ):
        self.동산여부 = 동산여부



class 물권(LegalRight):
    """민법에서 정의된 물권법
    """
    def __init__(self, 대상물):
        self.대상물 = 대상물
        super().__init__(

class 채권(LegalRight):
    pass

class 소유권(물권):
    """
    """
    def __init__(self, 소유자, 소유물):
        assert isinstacne(소유자, 인)
        assert isinstacne(소유물, 물건)
        super().__init__(민법_제211조)
        self.소유자 = 소유자
        self.소유물 = 소유물
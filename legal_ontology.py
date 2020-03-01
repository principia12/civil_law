class LegalEntity:
    pass

class LegalRight:
    def __init__(self, 근거조항 = []):
        for 근거 in 근거조항:
            assert isinstance(근거, LegalStatement)
        self.근거조항 = 근거조항

class LegalRelation:
    pass

class LegalStatement:
    """법의 근거가 되는 조항을 적시하기 위한 wrapper class
    """
    def __init__(self, **kargs):
        assert all([e in ['법령', '장', '절', '조', '항', '목', '조문', '항목'] for e in kargs])
        for k, v in kargs.items():
            setattr(self, k, v)

        if '조문' in kargs:
            from nlp_modules.preprocessor import Tokenizer, basic_tokenizer
            from korlib.korean_dict import 역접접속사

            sents = basic_tokenizer(self.조문)
            if len(sents) == 2:
                if sents[1].형태소분석[0] in 역접접속사:
                    # 본문/단서 관계 나중에 넣어줘야 할듯?
                    self.본문 = sents[0]
                    self.단서 = sents[1]
                self.전단 = sents[0]
                self.후단 = sents[1]
                self._1문 = sents[0]
                self._2문 = sents[1]
            else:
                for idx in sents:
                    setattr(self, '_%d문', sents[idx])

    def __call__(self, args):
        if re.match(r'제%d조', args):
            pass

    def __str__(self):
        법령 = self.법령
        장 = self.장
        try:
            절 = self.절
        except AttributeError:
            절 = ''
        조 = self.조
        조문 = self.조문

        if 절 == '':
            # return f'{법령}\n{장}장 {조}조\n{조문}'
            return '%s\n%d장 %d조\n%s'%(법령, 장, 조, 조문)

        # return f'{법령}\n{장}장 {절}절 {조}조\n{조문}'
        return '%s\n%d장 %d절 %d조\n%s'%(법령, 장, 절, 조, 조문)

if __name__ == '__main__':
    l = LegalStatement(법령 = '민법',
                       장 = '3',
                       절 = '1',
                       조 = '211',
                       조문 = '소유자는 법률의 범위내에서 그 소유물을 사용, 수익, 처분할 권리가 있다.')

    print(l)
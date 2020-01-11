class Tokenizer:
    def __init__(self, sentence_divider, sentence_tokenizer, sentence_parser):
        """문장 종합 전처리기
        """
        self.sentence_divider = sentence_divider
        self.sentence_tokenizer = sentence_tokenizer
        self.sentence_parser = sentence_parser

    def __call__(self, text):
        """주어진 텍스트 분석 후 출력
        """
        sents = self.sentence_divider(text)
        res = {}
        for idx, sent in enumerate(sents):
            res[idx] = ProcessedResult(sent,
                        self.sentence_tokenizer(sent),
                        self.sentence_parser(sent))

        return res

class ProcessedResult:
    def __init__(self, sent, tokenized_result, parsed_result):
        self.sent = sent
        self.tokenized_result = tokenized_result
        self.parsed_result = parsed_result
        self.형태소분석 = tokenized_result
        self.구문분석 = parsed_result

basic_tokenizer = Tokenizer(\
    lambda x:x.split('.')[:-1],
    lambda x:x.split(),
    lambda x:x)

if __name__ == '__main__':
    text = '미성년자가 법률행위를 함에는 법정대리인의 동의를 얻어야 한다. 그러나 권리만을 얻거나 의무만을 면하는 행위는 그러하지 아니하다.'
    res = basic_tokenizer(text)

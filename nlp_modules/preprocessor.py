import os

from __init__ import *
from code import interact

from koalanlp.Util import initialize, finalize
from koalanlp.proc import SentenceSplitter, Tagger, Parser
from koalanlp import API

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

class KoalaTokenizer:
    def __init__(self, api_name = 'HNN'):
        try:
            self.API = eval('API.%s'%api_name)
        except AttributeError:
            assert False, 'No such api'
        self.splitter = lambda x : None
        self.tagger = lambda x : None
        self.parser = lambda x : None

    def __enter__(self):
        initialize(java_options="-Xmx4g", hnn='LATEST', KKMA="2.0.4", ETRI="2.0.4")
        try:
            self.splitter = SentenceSplitter(self.API)
        except AttributeError:
            print('SentenceSplitter not provided for %s'%self.API)

        try:
            self.tagger = Tagger(self.API)
        except AttributeError:
            print('tagger not provided for %s'%self.API)

        try:
            self.parser = Parser(self.API)
        except AttributeError:
            print('parser not provided for %s'%self.API)

        return self

    def __exit__(self, exc_type, value, traceback):
        if exc_type is not None:
            print(exc_type)
            finalize()
            return False
        finalize()
        print('Finalize JVM')
        return True


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

# 한나눔 parser wrapper

# initialize(java_options="-Xmx4g", hnn='LATEST', KKMA="2.0.4", ETRI="2.0.4")

# splitter = SentenceSplitter(API.HNN)
# tagger = Tagger(API.HNN)
# parser = Parser(API.HNN)

# finalize()

# hnn_tokenizer = Tokenizer(splitter, tagger, parser)

if __name__ == '__main__' and False:
    text = '미성년자가 법률행위를 함에는 법정대리인의 동의를 얻어야 한다. 그러나 권리만을 얻거나 의무만을 면하는 행위는 그러하지 아니하다.'
    res = basic_tokenizer(text)

    # initialize(java_options="-Xmx4g", hnn='LATEST', KKMA="2.0.4", ETRI="2.0.4")

    # 한나눔 parser wrapper

    # splitter = SentenceSplitter(API.HNN)
    # tagger = Tagger(API.HNN)
    # parser = Parser(API.HNN)

    finalize()

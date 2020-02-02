from pprint import pprint
from code import interact
from legal_statements import 민법조항들
from nlp_modules.preprocessor import KoalaTokenizer as T

def 조항_분석():
    """
    """
    with T() as processor:

        for 조항 in 민법조항들()[100:110]:
            print('-----------------')
            print(조항.조문)

            for sent in processor.splitter(조항.조문):
                tagged_result = processor.tagger(sent)
                가정 = []
                결과 = []

                for sent in tagged_result:
                    flag = False
                    for word in sent.words:
                        for morph in word.morphemes:
                            print(morph)



                        # interact(local = locals())
                    # s

if __name__ == '__main__':
    조항_분석()

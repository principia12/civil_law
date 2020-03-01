from pprint import pprint
from code import interact

from legal_statements import 민법조항들
from nlp_modules.preprocessor import KoalaTokenizer as T
from ds.tree import Tree
from util import split_lst, lcs

def 조항_분석():
    """
    """
    with T('etri') as processor:

        # for 조항 in 민법조항들()[240:260]:
            # print('-----------------')
            # print(조항.조문)

            # for sent in processor.splitter(조항.조문):
                # tagged_result = processor.tagger(sent)

                # 가정 = []
                # 결과 = []

                # for parse_tree in processor.parser(sent):
                    # print(parse_tree.getSyntaxTree().getTreeString())

                # for sent in tagged_result:
                    # for word in sent.words:
                        # for morph in word.morphemes:
                            # print(morph)
        text = '20년간 소유의 의사로 평온, 공연하게 부동산을 점유하는 자는 등기함으로써 그 소유권을 취득한다.'
        for parse_tree in processor.parser(text):
            print(parse_tree.getSyntaxTree().getTreeString())
            # print(parse_tree.getDependencyTree().

# def

def demo_20200216():
    """
    input : 매매는 당사자 일방이 재산권을 상대방에게 이전할 것을 약정하고 상대방이 그 대금을 지급할 것을 약정함으로써 그 효력이 생긴다.

    매매는

            당사자 일방이 재산권을 상대방에게 이전할 = ㄱ
            상대방이 그 대금을 지급할 = ㄴ
        것(ㄱ -고  ㄴ)을 약정하-
    으로써
    그 효력이 생긴다.
    >>

    매매는
        and
            당사자 일방이 재산권을 상대방에게 이전할 것
            상대방이 그 대금을 지급할 것
        약정함으로써
    그 효력이 생긴다.

    >>

    매매는
        and
            x = 이전(당사자 일방, 재산권, 상대방)
            y = 지급(상대방, 그 대금)
        약정함으로써
        (x and y) -> z
        z를 약정함으로써
    그 효력이 생긴다.


    input : 매도인은 매수인에 대하여 매매의 목적이 된 권리를 이전하여야 하며 매수인은 매도인에게 그 대금을 지급하여야 한다.
    >>
    and
        OB 매도인은 매수인에 대하여 매매의 목적이 된 권리를 이전한다
        OB 매수인은 매도인에게 그 대금을 지급한다
    >>
    and
        OB 이전(매도인, 매수인, 매매의 목적이 된 권리)
        OB 지급(매수인, 매도인, 그 대금,)
    >>
    and
        OB 이전(매도인, 매수인, (매매의 목적이 된 권리:x))
        OB 지급(매수인, 매도인, x의 대금,)

    OB 이전(매도인, 매수인, (매매의 목적이 된 권리:x))





    input : 20년간 소유의 의사로 평온, 공연하게 부동산을 점유하는 자는 등기함으로써 그 소유권을 취득한다.
    >>
    (부동산:a)을 평온, 공연하게 20년간 소유의 의사로 (점유:x)하다
    (x인 자:y)는 등기함으로써 그 소유권을 취득한다

    (x인 자는 등기한다 >> (x이며 등기한:z)인 자)
    z인 자는 그 소유권을 취득한다

    >>
    취득(z, 그 소유권)

    >>
    if 자 is z: then 취득(자, a의 소유권)

    ◆ 초기값: if「점유자」등기 then 취득|소유권(△△△)




    $$
    1. 법률의 “그 소유권을 취득” 이라는 문언으로부터 “점유한 부동산의 소유권을 취득”이라는 점을 추론.
    2. 등기의 종류를 결정해야 하는데, 결과가 점유부동산의 소유권 취득이니 “이전등기|소유권(부동산)”라고 추론.
    3. 이전등기의 의무자가 기재되어 있지 않은데, 점유자가 소유권을 취득한다는 것은 반대로, 현재 소유자가 소유권을 잃는다는 것이므로 의무자는 현소유자라는 것을 추론.
    4. 등기함으로써 취득한다는 말은 그렇게 하는 것이 허용된다는 의미이므로, 권리(PE)형태로 변형.
    5. 이를 의무(OB) 형태로 변형.
    $$

    0. if「점유자」등기 then 취득|소유권(△△△)
    1. if「점유자」등기 then 취득|소유권(부동산)
    2. if「점유자」이전등기|소유권(부동산) then 취득|소유권(부동산)
    3. if「점유자」이전등기|소유권(부동산)「현소유자」 then 취득|소유권(부동산)
    4. PE「점유자」이전등기|소유권(부동산)「현소유자」
    5. OB「현소유자」이전등기절차이행|소유권(부동산)「점유자」

    ◆ 결과값: OB「현소유자」이전등기절차이행|소유권(부동산)「점유자」

    """
    text = '20년간 소유의 의사로 평온, 공연하게 부동산을 점유하는 자는 등기함으로써 그 소유권을 취득한다.'

    text = '20년간 소유의 의사로 평온, 공연하게 부동산을 점유하는 자는 등기함으로써 그 소유권을 취득한다.'

    text = '매매는 당사자 일방이 재산권을 상대방에게 이전할 것을 약정하고 상대방이 그 대금을 지급할 것을 약정함으로써 그 효력이 생긴다.'

    log = open('log.txt', 'w+', encoding = 'utf-8')

    def fprint(s):
        print(s)
        print(s, file = log)

    # with T('KKMA') as processor: # for dependency tree
    with T('HNN') as processor: # for dependency tree
        fprint('start : %s'%text)
        sent = processor.tagger(text)[0]

        morphemes = []

        for word in sent:
            for morph in word.morphemes:
                morphemes.append(morph)

        splited_morphemes = split_lst(morphemes,
                    delim_func = lambda x:x.getTag().name == 'JC')

        if len(splited_morphemes) == 1:
            return splited_morphemes

        for 선행절, 후행절 in zip(splited_morphemes[:-1],
                             splited_morphemes[1:],):
            a, b = lcs(선행절, 후행절, key = lambda x:x.getTag())

            for m_a, m_b in zip(a,b):
                print(str(m_a) + '\t' + str(m_b))

            interact(local = locals())

        # for parse_tree in processor.parser(text):

            # for dep in parse_tree.getDependencies():
                # print(dir(dep))
            # lst = parse_tree.getDependencies()
            # print(parse_tree.getSyntaxTree().getTreeString())
            # Tree.from_koala_syntaxtree(parse_tree.getSyntaxTree())


    log.close()

if __name__ == '__main__':
    demo_20200216()

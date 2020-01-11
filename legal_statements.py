import os
import re
from legal_ontology import LegalStatement

def 민법_parser(file_path = os.path.join('..', 'assets', '민법전문.txt')):

    편_패턴 = re.compile(r'제([0-9]*)편 ([가-힣]*)')
    장_패턴 = re.compile(r'제([0-9]*)장 ([가-힣]*)')
    절_패턴 = re.compile(r'제([0-9]*)절 ([가-힣]*)')
    조_패턴 = re.compile(r'제([0-9]*)조\(([가-힣 ]*)\)')

    항_기호 = {'①' : 1, }

    patterns = [편_패턴, 장_패턴, 절_패턴, 조_패턴]

    with open(file_path, 'r', encoding = 'utf-8') as f:
        편 = 0
        장 = 0
        절 = 0
        조 = 0
        항 = 0
        호 = 0

        for line in f.readlines():
            line = line.strip()

민법_제3조 = LegalStatement(법령 = '민법',
                       장 = '2',
                       절 = '1',
                       조 = '3',
                       조문 = '사람은 생존한 동안 권리와 의무의 주체가 된다.')

민법_제98조 = LegalStatement(법령 = '민법',
                       장 = '4',
                       조 = '3',
                       조문 = '본법에서 물건이라 함은 유체물 및 전기 기타 관리할 수 있는 자연력을 말한다.')

민법_제211조 = LegalStatement(법령 = '민법',
                       장 = '3',
                       절 = '1',
                       조 = '211',
                       조문 = '소유자는 법률의 범위내에서 그 소유물을 사용, 수익, 처분할 권리가 있다.')

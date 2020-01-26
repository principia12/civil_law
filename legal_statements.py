import os
import re
from legal_ontology import LegalStatement

def 민법_parser(file_path = os.path.join('assets', '민법전문')):
    법령 = '민법'
    편_패턴 = re.compile(r'제([0-9]*)편 ([가-힣]*)')
    장_패턴 = re.compile(r'제([0-9]*)장 ([가-힣]*)')
    절_패턴 = re.compile(r'제([0-9]*)절 ([가-힣]*)')
    조_패턴 = re.compile(r'제([0-9]*)조\(([가-힣 ,]*)\) (.*)')
    
    start = chr(ord('①')-1)
    항_기호 = {}
    res = []
    for i in range(15):
        항_기호[chr(ord(start) + i)] = i
    
    patterns = [편_패턴, 장_패턴, 절_패턴, 조_패턴]

    with open(file_path, 'r', encoding = 'utf-8') as f:
        편 = 0
        장 = 0
        절 = 0
        조 = 0
        항 = 0
        호 = 0

        while True:
            line = f.readline()
            if line == '':
                break
            line = line.strip()
            
            if re.search(편_패턴, line):
                편 += 1
                print('편 : %d'%편)
                절 = 0
                장 = 0
                
            elif re.search(장_패턴, line):
                장 += 1
                print('장 : %d'%장)
                절 = 0
                
            elif re.search(절_패턴, line):
                절 += 1
                print('절 : %d'%절)
                
            elif re.search(조_패턴, line):
                # 조 += 1
                # print('조 : %d'%조)
                # print('-----------')
                # print(line)
                조 = int(re.search(조_패턴, line).group(1))
                항목 = re.search(조_패턴, line).group(2)
                조문 = [re.search(조_패턴, line).group(3)]
                # print(line)
                if 조문[0].startswith('①'):
                    i = 0
                    while True:
                        line = f.readline().strip()
                        
                        if line != '' and line[0] in 항_기호:
                            조문.append(line)
                        else: # 조문신설시점 파악 가능
                            pass
                        
                        if not (line == '' or line[0] in 항_기호):
                            break
                        # break
                for idx, 조 in enumerate(조문):
                    res.append(LegalStatement(법령 = 법령, 장 = 장, 절 = 절, 조 = 조, 항 = idx+1, 조문 = 조[1:], 항목 = 항목))
    return res
    
    
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
                       
if __name__ == '__main__':
    res = 민법_parser()
    print(len(res))

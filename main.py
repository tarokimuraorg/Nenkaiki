import re

def convertToHankaku(zenkaku : str) -> str:

    zenkaku_data = [0xff01 + i for i in range(94)]
    hankaku_data = [0x21 + i for i in range(94)]
    data = {zenkaku_data[i]:hankaku_data[i] for i in range(94)}

    return zenkaku.translate(data)

def convertToZenkaku(hankaku : str) -> str:

    zenkaku_data = [0xff01 + i for i in range(94)]
    hankaku_data = [0x21 + i for i in range(94)]
    data = {hankaku_data[i]:zenkaku_data[i] for i in range(94)}

    return hankaku.translate(data)

class WarekiError(Exception):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return 'Enter Seireki.'

if __name__ == '__main__':

    while True:

        try:
            in_year = input('故人が亡くなられた年を西暦で入力してください : ')
            in_year = str(in_year)

            if re.search('令和',in_year) or re.search('平成',in_year) \
                or re.search('昭和',in_year) or re.search('大正',in_year) \
                or re.search('明治',in_year):

                raise WarekiError()

            in_year = re.sub(r'\D','',in_year)
            in_year = convertToHankaku(str(in_year))

            out_year = int(in_year)
            dct_nenkaiki = {'１周忌' : out_year + 1}
            dct_nenkaiki['３回忌'] = out_year + 2
            dct_nenkaiki['７回忌'] = out_year + 6
            dct_nenkaiki['１３回忌'] = out_year + 12
            dct_nenkaiki['１７回忌'] = out_year + 16
            dct_nenkaiki['２３回忌'] = out_year + 22
            dct_nenkaiki['２７回忌'] = out_year + 26
            dct_nenkaiki['３３回忌'] = out_year + 32
            dct_nenkaiki['５０回忌'] = out_year + 49
            
            for key,value in dct_nenkaiki.items():
                print('{} : {}年'.format(key,convertToZenkaku(str(value))))
            
        except ValueError:
            print('値が不正です。 例) 没年が2011年の場合 : 「2011」と入力してください。')
        except WarekiError:
            print('没年は西暦で入力してください。')

        else:
            break

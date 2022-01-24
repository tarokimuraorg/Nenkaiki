import re
from StringConvertor import StringConvertor
import NenkaikiCalculator as nc
from CustomError import WarekiError

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
            sc = StringConvertor()
            in_year = sc.toHankaku(str(in_year))

            out_year = int(in_year)
            dct_nenkaiki = nc.results(out_year)

            for key,value in dct_nenkaiki.items():
                print('{} : {}年'.format(key,sc.toZenkaku(str(value))))
            
        except ValueError:
            print('値が不正です。 例) 没年が2011年の場合 : 「2011」と入力してください。')

        except WarekiError:
            print('没年は西暦で入力してください。')

        else:            
            break

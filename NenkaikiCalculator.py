def results(year_of_death : int) -> dict :

    dct_nenkaiki = {'１周忌' : year_of_death + 1}
    dct_nenkaiki['３回忌'] = year_of_death + 2
    dct_nenkaiki['７回忌'] = year_of_death + 6
    dct_nenkaiki['１３回忌'] = year_of_death + 12
    dct_nenkaiki['１７回忌'] = year_of_death + 16
    dct_nenkaiki['２３回忌'] = year_of_death + 22
    dct_nenkaiki['２７回忌'] = year_of_death + 26
    dct_nenkaiki['３３回忌'] = year_of_death + 32
    dct_nenkaiki['５０回忌'] = year_of_death + 49

    return dct_nenkaiki

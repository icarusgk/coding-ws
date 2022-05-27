inp1 = 'common name:dog, species:Canis familiaris'

_d_list = [keyword.split(':') for keyword in inp1.split(', ')]
domestic_animal = {key: value for key, value in _d_list}
_w_list = [keyword.split(':') for keyword in inp1.split(', ')]
wild_animal = {key: value for key, value in _w_list}

print(_d_list)
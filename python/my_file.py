#!/usr/bin/python
def gen_readme(quote=''):
  with open('README.md', 'w') as file:
    file.write('# This is a header\n')


gen_readme()
print('Your README file has been generated!')


err = {
  1: lambda construction_name: f'Too many spaces after {construction_name}'
}

print(err[1]('def'))


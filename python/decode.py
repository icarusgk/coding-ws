import argparse

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')

args = parser.parse_args()

filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()

decode_Caesar_cipher(encoded_text, -13)
opened_file.close()

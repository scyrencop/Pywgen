
import itertools
import click
import os
import time

# Global Variable

PATH = 'wordlist/'
FILENAME = 'password.txt'


def CheckPathExist(path):
	if not os.path.exists(path) and len(path) > 1:
		os.makedirs(path)


CheckPathExist(PATH)


def generatorInterv(chrs, min, max, path):
    min_length = min
    max_length = max
    fob = open(path, 'a')
    for n in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=n):
            word = ''.join(xs)
            fob.write(word)
            fob.write('\n')
    fob.close()


def generator(chrs, len_word, path):
    fob = open(path, 'a')
    total_words = 0
    for xs in itertools.product(chrs, repeat=len_word):
        word = ''.join(xs)
        fob.write(word)
        fob.write('\n')
        total_words += 1
    fob.close()
    print('> Total of : '+str(total_words)+' Words')


chrs_lower = 'abcdefghijklmnopqrstuvwxyz'
chrs_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'


@click.command()
@click.option('-len', default=1, help='lenth of word')
@click.option('-char', default='az', help='az - AZ - 09 separate by "," default value az ')
# @click.option('-char', prompt='Your Char', help='Choose the Char')
def main(char, len):

    start = time.time()

    glob_char = ''
    print('--------')
    if(char.find('az') != -1):
        glob_char += chrs_lower
    if(char.find('AZ') != -1):
        glob_char += chrs_upper
    if(char.find('09') != -1):
        glob_char += numbers

    generator(glob_char, len, PATH+FILENAME)

    end = time.time()
    time_process = end - start
    print("> Process Times : "+"%.3f" % time_process + ' seconds')
    print("> Path : '"+PATH+FILENAME+"' is Successfully Generated")

    print('--------')


if __name__ == "__main__":
    main()

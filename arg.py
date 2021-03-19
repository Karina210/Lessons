from time import sleep
from random import randint
import sys
import argparse
import os




def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)  # это каждый столбец. последний пункт - важно или нет
    parser.add_argument('-ln', '--last-name', required=True)

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    arg()







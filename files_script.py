
import argparse
import os





def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-br', '--born')

    args = parser.parse_args()

    with open('users.csv', 'a') as file:
        file.write(f'{args.first_name},{args.last_name},{args.born}\n')


def os_testing():
    file_path = os.path.realpath('./files')
    print(file_path)

    dir_name = os.path.dirname(file_path)
    print(dir_name)

    os.mkdir('test-mkdir')  #создаст этот файл


if __name__ == '__main__':
    arg_parse()
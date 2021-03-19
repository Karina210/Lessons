import sys

def main():
    numbers = sys.argv[1:]
    sum = 0
    for item in numbers:
        if not item.isdigit():
            continue

        sum += int(item)

    print(sum)

if __name__ == '__main__':
    main()
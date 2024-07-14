def main():
    args = get_args()
    for letter in args.letter:
        print(letter)
    for line in args.file:
        print(line, end='')
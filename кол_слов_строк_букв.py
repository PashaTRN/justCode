with open('file.txt', 'r', encoding='utf-8') as f:
    lines = 0
    words = 0
    letters = 0
    for line in f:
        lines += 1
        words += len(line.split())
        letters += sum(map(lambda x: 1 if x.isalpha() else False, line))

print('Input file contains:', str(letters) + ' letters',
      str(words) + ' words', str(lines) + ' lines', sep='\n')

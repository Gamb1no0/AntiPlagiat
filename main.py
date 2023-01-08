import argparse
parser = argparse.ArgumentParser()
#Позиционные аргументы
parser.add_argument('--input', type=str, help="input file path")
parser.add_argument('--output', type=str, help="output file path")
args = parser.parse_args()

def remove_empty_lines(lines):
    try:
        while True:
            lines.remove('\n')
    except ValueError:
        pass
    return lines
def removing_comments1(lines):
    i = 0
    while i < len(lines):
        if str.startswith(lines[i], '"""') and str.endswith(lines[i], '"""'):
            del lines[i]
        else:
            i += 1
def removing_comments2(lines):
    i = 0
    start = 0
    end = 0
    while i < len(lines):
        if str.startswith(lines[i], '"""'):
            start = i
        if str.endswith(lines[i], '"""'):
            end = i
            del lines[start:end+1]
        else:
            i += 1
def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + 1)  # transposition

    return d[lenstr1 - 1, lenstr2 - 1]

with open(args.input, 'r') as f:
    file1 = open(args.input, 'r', encoding='utf-8')
    lines1 = file1.readlines()
    #удаляю все пустые строки
    remove_empty_lines(lines1)
    lines1 = list(map(str.strip, lines1))
    removing_comments1(lines1)
    removing_comments2(lines1)
    for line in lines1:
        print(line)
    file1.close()

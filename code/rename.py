#!/usr/bin/env python3
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 3:
        print('Input and output file names are required')
        return
    with open(sys.argv[1], 'r') as infile:
        # csv.reader ругается на слишком длинные поля, а pandas - оверкилл для такого задания.
        # Проще распарсить файл вручную
        data = [line.split('\t') for line in infile]
    state_names = [
        'CTCF',
        'Heterochromatin',
        'Unknown_1',
        'Exon?',
        'Unknown_2',
        'Unknown_3',
        'Unknown_4',
        'Unknown_5',
        'Active_promoter',
        'Active_promoter_2',
    ]
    for line in data[2:]:  # пропускаем заголовок
        line[3] = state_names[int(line[3]) - 1]
    with open(sys.argv[2], 'w') as outfile:
        outfile.write(''.join('\t'.join(line) for line in data))


if __name__ == '__main__':
    main()

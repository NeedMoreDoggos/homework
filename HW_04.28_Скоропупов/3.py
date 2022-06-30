from pathlib import Path
import json


def file_reader(path=None):
    path = path or Path().cwd()
    keys = None
    texts = dict()

    for file in Path(path).glob('**/*.txt'):
        if file.name == 'keywords.txt':
            with open(file, 'r', encoding='utf-8') as fin:
                keys = fin.read().split()
        else:
            with open(file, 'r', encoding='utf-8') as fin:
                texts[file.name] = [line.strip() for line in fin.read().split('\n')]

    return (keys, texts) if keys else (None, None)


def to_json(value):
    with open('to_json.txt', 'a', encoding='utf-8') as file:
        file.write(json.dumps(value, indent=4, ensure_ascii=False))


def finder(path=None, context=0):
    keywords, texts = file_reader(path)
    summary = list()

    for keyword in keywords:
        for name, text in texts.items():
            for i in range(len(text)):
                if keyword in text[i]:
                    summary.append(
                        {
                            'filename': name,
                            'line_number': i,
                            'keyword': keyword,
                            'context': context,
                            'text': text[i - context if i - context > 0 else 0: i + context + 1]
                        }
                    )

    to_json(summary)


finder(path=None, context=4)


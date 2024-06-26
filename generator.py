#!python
import json
import os
from urllib.request import urlopen
from random import choices as sample
from random import seed

if 'words.json' in os.listdir():
    with open('words.json', 'r') as f:
        words = json.load(f)
else:
    with urlopen('https://raw.githubusercontent.com/awong234/job-title-generator/main/words.json') as f:
        text = f.read().decode('utf-8')
    words = json.loads(text)

def generate_job_title(choices = None):
    if choices is None:
        choices = ["prefix", "adjective", "superlative", "job type", "title", "suffix"]
        # Sample from the space of choices, turn on and off randomly
        selection = sample([True, False], k = len(choices))
        selection = {x: y for x,y in zip(choices, selection)}
        # But keep job type active
        selection['job type'] = True
        choices = [ x for x,y in selection.items() if y]

    # Pick randomly from each category
    my_sample = [sample(words[x])[0] for x in choices]
    my_sample = ' '.join(my_sample)
    rank = sample([x for x in range(1,30)])[0]
    rank = int_to_roman(rank)
    my_sample = my_sample + ' ' + rank
    return my_sample

ROMAN = [
    (1000, "M"),
    ( 900, "CM"),
    ( 500, "D"),
    ( 400, "CD"),
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),
]

def int_to_roman(number):
    result = ""
    for (arabic, roman) in ROMAN:
        (factor, number) = divmod(number, arabic)
        result += roman * factor
    return result

print(generate_job_title())

# titles = []
# for i in range(0, 1000):
#     seed(i)
#     titles.append(generate_job_title())
#     print(i, titles[i])

# titles_sorted = titles.copy()
# titles_sorted.sort(key = lambda x: len(x))
# titles_sorted

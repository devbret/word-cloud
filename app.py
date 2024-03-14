import os
import json
from collections import Counter
from nltk import ngrams, corpus
from nltk.tokenize import word_tokenize

directory = 'path/to/your/directory/'

stopwords = set(corpus.stopwords.words('english'))
additional_common_words = {'add', 'additional', 'stop', 'words', 'here'}
stopwords.update(additional_common_words)

def read_and_concatenate_txt_files(directory):
    all_text = ""
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                all_text += " " + file.read()
    return all_text

def find_common_phrases(text):
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stopwords and word.isalpha()]
    two_grams = ngrams(filtered_words, 2)
    phrases = [' '.join(gram) for gram in two_grams]
    return Counter(phrases).most_common(2000)


def create_json_for_word_cloud(common_phrases):
    return [{'text': phrase, 'size': frequency} for phrase, frequency in common_phrases]

all_text = read_and_concatenate_txt_files(directory)
common_phrases = find_common_phrases(all_text)
json_structure = create_json_for_word_cloud(common_phrases)

with open('word_cloud_data.json', 'w', encoding='utf-8') as f:
    json.dump(json_structure, f, ensure_ascii=False, indent=4)

print("JSON file for word cloud visualization has been created.")

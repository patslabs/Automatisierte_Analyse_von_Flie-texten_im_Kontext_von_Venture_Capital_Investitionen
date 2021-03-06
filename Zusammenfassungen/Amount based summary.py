import re
import nltk
import heapq
import glob
import numpy
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize


def read_file():
    with open("deepcode4.txt", "r", encoding="utf8") as textfile:
        text = textfile.read()
        changedtext = re.sub("TITLE:", " ", text)
        text_for_processing = re.sub("TEXT:", " ", changedtext)
    return text_for_processing


def collect_data(directory):
    #Takes multiple files and summarizes them into one Text. Returns that text.
    file_list = glob.glob(directory)
    #loads every file from the given directory
    big_text = ""
    for file in file_list:
        with open(file, "r", encoding="utf8") as textfile:
            text = textfile.read()
            changedtext = re.sub("TITLE:", " ", text)
            text_for_processing = re.sub("TEXT:", " ", changedtext)
            big_text = big_text + text_for_processing
    return big_text


def calc_lang_ratios(text):
    #finds how many unique stopwords are existing in the text per language
    language_amounts = {}
    single_words = wordpunct_tokenize(text)
    words = [word.lower() for word in single_words]

    for language in stopwords.fileids():
        stops = []
        for item in stopwords.words(language):
            stops.extend(wordpunct_tokenize(item))
            stopwords_set = set(stops)
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        language_amounts[language] = len(common_elements)
    return language_amounts


def find_language(text):
    #finds the most common language
    amount = calc_lang_ratios(text)
    most_amount_of_language = max(amount, key=amount.get)
    return most_amount_of_language


def preprocessing(text):
    #Create a summary by finding the most important sentences

    text = re.sub(r'\s+', ' ', text)
    #The variable "text" has original text, used to work with the whole sentence.
    #The variable "formatted_text" is cleaned, used to work only with the words.
    formatted_text = re.sub('[^a-zA-Z]', ' ', text)
    formatted_text = re.sub(r'\s+', ' ', formatted_text)

    #parse text into sentences
    sentence_list = nltk.sent_tokenize(text)
    return sentence_list, formatted_text


def calculate_word_frequencies(formatted_text):
    #create a dict of all words besides the stopwords with their frequency
    word_frequencies = {}
    stop_words = stopwords.words(find_language(formatted_text))
    for word in nltk.word_tokenize(formatted_text):
        if word not in stop_words:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    # Change the word frequency value from an absolute to a relative one, depending on the length of the sentence.
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)
    return word_frequencies


def sentence_scoring(sentence_list):
    #score the sentences
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 50:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    for sent in sentence_scores.keys():
        sentence_scores[sent] = sentence_scores[sent] / len(sent.split(" "))
    return sentence_scores


def create_summary(sentence_scores, number_of_sentences):
    #prints out the top sentences
    summary_sentences = heapq.nlargest(number_of_sentences, sentence_scores, key=sentence_scores.get)
    return summary_sentences


def stats_of_sentence_lists(sentence_list):
    #Calculates stats to compare different selection algorithms. Not used in the final algorithm.
    sentence_length = {}
    for sentence in sentence_list:
        sentence_length[sentence] = len(sentence)
    laengsterSatz = max(sentence_length.values())

    print("MAx:" + str(laengsterSatz))
    average = numpy.average(list(sentence_length.values()))
    print("Average: " + str(average))
    median = numpy.median(list(sentence_length.values()))
    print("median. " + str(median))
    for sentence, length in sentence_length.items():
        if length == 753:
            print(sentence)
    return


def create_summary_file(text, summary_filename):
    with open(summary_filename, "w") as file:
        file.writelines(text)
    return


# ------------------------------------
# Variables:
directory = "C:\\DATA\\NLP Testing\\medium test data, deepcodeAI\\deepcode test//*.txt" # //* searches for all files.
number_of_sentences_in_summary = 3
summary_file_name = "SUMMARY.txt"

# Calls:
# 1. Get the Textdata
Text = collect_data(directory)

# 2. Get the processing data
sentence_list, formatted_text = preprocessing(Text)

# 2.1(optional) print some stats about the sentencces
# stats_of_sentence_lists(sentence_list)

# 3. Calculate the frequency of the words
word_frequencies = calculate_word_frequencies(formatted_text)

# 4. Score the sentences
sentence_scores = sentence_scoring(sentence_list)

# 5. Create the text for the summary
summary_sentences = create_summary(sentence_scores, number_of_sentences_in_summary)
summary_text = ' '.join(summary_sentences)
# 5.1 (optional) print stats about the summary sentences:
# stats_of_sentence_lists(summary_sentences)

# 6. Create summary_file
create_summary_file(summary_text, summary_file_name)




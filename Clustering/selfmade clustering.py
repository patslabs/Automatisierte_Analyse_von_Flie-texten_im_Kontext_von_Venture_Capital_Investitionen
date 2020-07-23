import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.cluster import KMeans

def load_data(file):
    # Load the data
    df = pd.read_csv(file, header=0, encoding="utf8")
    # drop the Nan rows, empty rows deleted
    df.dropna(inplace=True)
    # rename the axis to have a pandas conform label
    df.set_axis(["Affe"], axis=1, inplace=True)
    return df


def process(string):
#    deutscher test
#    import de_core_news_sm
#    nlp = de_core_news_sm.load()

    lemma = WordNetLemmatizer()
    stopword_set = stopwords.words('english')
#    nlp = de_core_news_sm.load()
    string = ' ' + string + ' '
    string = ' '.join([word if word not in stopword_set else '' for word in string.split()])
    string = re.sub('\@\w*', ' ', string)
    string = re.sub('\.', ' ', string)
    string = re.sub("[,#'-\(\):$;\?%]", ' ', string)
    string = re.sub("\d", ' ', string)
    string = string.lower()
    string = re.sub(r'[^\x00-\x7F]+', ' ', string)
#    doc = nlp(string)
#    string = " ".join(token.lemma_ for token in doc)
    string = " ".join(lemma.lemmatize(word) for word in string.split())
    string = re.sub('( [\w]{1,2} )', ' ', string)
    string = re.sub("\s+", ' ', string)
    return string.split()


def pre_process_data(df):
    # drop the duplicate values of news
    df.drop_duplicates(keep='last', inplace=True)
    # reindex the data frame
    df.index = range(0, len(df))
    # apply the process function to the news titles
    df['text_l'] = df['Affe'].apply(process)
    df_new = df
    return df_new


def doc_2_vec_model(df_new):
    # Train the model
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(list(df_new['text_l']))]
    model = Doc2Vec(documents, vector_size=25, window=2, min_count=1, workers=4)
    # appending all the vectors in a list
    X = []
    for i in range(len(model.docvecs)):
        X.append(model.docvecs[i])
        print(model.docvecs[i])
    return X


def find_clusters(X, df_new):
    # create the kmeans object withe vectors created previously
    kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
    print(kmeans.labels_)
    # craete a dictionary to get cluster data, will be 4 clusters
    clusters = {0: [], 1: []}
    for i in range(len(kmeans.labels_)):
        clusters[kmeans.labels_[i]].append(' '.join(df_new.loc[i, 'text_l']))
    return clusters

# ---------------------------------------------------------------------
# Variables:
file = "Name.csv" # file from which to load text data. Has to be CSV

# Calls:
# 1.: Load Data:
df = load_data(file)
# 2.: Pre process Data using the process function:
df_new = pre_process_data(df)
# 3.: Create the Vector model
X = doc_2_vec_model(df_new)
# 4.: Compute the Clusters
clusters = find_clusters(X, df_new)
# 5.: Output:
print(clusters)



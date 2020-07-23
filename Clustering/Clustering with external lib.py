from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import os


def get_data_set(directory):
    dataset = []
    os.chdir(directory)

    for file in os.listdir("."):
        if os.path.isfile(file):
            print(file)
            with open(file, "r") as txtfile:
                text = txtfile.read()
            dataset.append(text)
    print(dataset)
    return dataset


def doc_2_ve_model(documents, true_k):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=150, n_init=1)
    model.fit(X)
    return model, vectorizer


def export_data(model, vectorizer, true_k):
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    print(type(order_centroids))
    print(model.labels_)
    for i in range(true_k):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind])
    return


def prediction(vectorizer, model, text):
    print("\n")
    print("Prediction")
    Y = vectorizer.transform([text])
    prediction = model.predict(Y)
    print(prediction)
    return


# -------------------------------------------------------
# Variabls:
directory = "C:\\DATA\\NLP Testing Clustering\\clustering test data"
amount_of_clusters = 2
prediction_text = "" # optional

# Calls:
# 1. Load Data:
dataset = get_data_set(directory)
# 2. Compute Doc2Vec
model, vectorizer = doc_2_ve_model(dataset, amount_of_clusters)
# 3. Print out the data:
export_data(model, vectorizer, amount_of_clusters)
# 4. Optional, do a prediction for another text:
# prediction(vectorizer, model, prediction_text)

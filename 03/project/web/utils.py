import docx
import re
import os
import nltk
import pickle
import pandas as pd
from nltk.corpus import stopwords
from django.conf import settings


nltk.download("stopwords")


job_vectorizer_file = os.path.join(
    settings.BASE_DIR, "./static/data/job_vectorizer.pickle"
)
job_vectorizer = pickle.load(open(job_vectorizer_file, "rb"))
job_matrix_file = os.path.join(settings.BASE_DIR, "./static/data/job_matrix.pickle")
job_matrix = pickle.load(open(job_matrix_file, "rb"))
ranker_file = os.path.join(settings.BASE_DIR, "./static/data/puestos.pickle")
ranker = pd.read_pickle(ranker_file)


def parseFileInformation(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)


def wrangler(raw):
    letras = re.sub("[^a-zA-ZáóéíúñÑ]", " ", raw)
    words = letras.lower().split()
    stops = set(stopwords.words("spanish"))
    meaningful_words = [w for w in words if not w in stops]
    return " ".join(meaningful_words)

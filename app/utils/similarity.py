from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def similarity_score(text1,text2):

    docs=[text1,text2]

    vectorizer=CountVectorizer().fit_transform(docs)

    vectors=vectorizer.toarray()

    score=cosine_similarity([vectors[0]],[vectors[1]])

    return score[0][0]
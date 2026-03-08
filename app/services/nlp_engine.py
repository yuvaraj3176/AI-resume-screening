from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def calculate_similarity(resume, job_desc):

    documents = [resume, job_desc]

    vectorizer = CountVectorizer().fit_transform(documents)

    vectors = vectorizer.toarray()

    similarity = cosine_similarity([vectors[0]], [vectors[1]])

    return similarity[0][0] * 100
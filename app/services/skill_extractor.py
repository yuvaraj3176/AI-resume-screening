import spacy

nlp = spacy.load("en_core_web_sm")

skills_db = [
"python",
"java",
"machine learning",
"deep learning",
"sql",
"data science",
"flask",
"django",
"tensorflow",
"pytorch"
]

def extract_skills(text):

    doc = nlp(text)

    found_skills = []

    for token in doc:
        if token.text.lower() in skills_db:
            found_skills.append(token.text)

    return list(set(found_skills))
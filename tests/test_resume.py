import unittest
from app.services.nlp_engine import calculate_similarity

class ResumeTest(unittest.TestCase):

    def test_similarity(self):

        resume="python flask machine learning"

        job="python developer flask"

        score=calculate_similarity(resume,job)

        self.assertTrue(score>=0)


if __name__=="__main__":
    unittest.main()
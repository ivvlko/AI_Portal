import pickle


def review_assessment(text_as_array):
    opener = open('Models/ai_handlers/movie_reviewer', 'rb')
    reviewer = pickle.load(opener)
    opener.close()
    score = reviewer.predict(text_as_array)
    return score[0]
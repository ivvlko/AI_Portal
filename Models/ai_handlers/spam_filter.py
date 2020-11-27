import pickle


def check_for_spam(text_as_array):
    opener = open('Models/ai_handlers/spam_detector.pickle', 'rb')
    detector = pickle.load(opener)
    opener.close()
    score = detector.predict(text_as_array)
    return score[0]


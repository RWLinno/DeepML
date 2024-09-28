import math


def softmax(scores: list[float]) -> list[float]:
    probabilities = [math.exp(i) for i in scores]
    sumexp = sum(probabilities)
    probabilities = [i / sumexp for i in probabilities]
    return probabilities

if __name__=="__main__":
    scores = [1, 2, 3]
    print(softmax(scores)) # [0.0900, 0.2447, 0.6652]
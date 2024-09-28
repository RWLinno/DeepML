import math

def sigmoid(z: float) -> float:
    result = 1/(1+math.exp(-z))
    return result

if __name__=="__main__":
    print(sigmoid(0)) # 0.5
import math
from numpy import *
from sklearn import tree

def main():
    training_data = genfromtxt('training.txt', delimiter=1)
    X_train = training_data[:, :57]
    Y_train = training_data[:, 58]

    test_data = genfromtxt('test.txt', delimiter=1)
    X_test = test_data[:, :57]
    Y_test = test_data[:, 58]

    build_adaboost(training_data, X_test, Y_test)

def build_adaboost(training_data, X_test, Y_test):
    
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=1)  # tree dumps
    # clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=2)  # depth 2 trees
    # initialize D
    D = ones(71) / 71
    print type(D)
    X_train = training_data[:, :57]
    Y_train = training_data[:, 58]
    for t in range(0, 100):
        clf = clf.fit(X=X_train, y=Y_train, sample_weight=D)
        h_t = clf.predict(X_train)
        error_t = calculate_error(D, h_t, training_data[:, 58])
        
        test_error = 1 - clf.score(X_test, Y_test)
        print test_error

        alpha = 0.5 * math.log1p(1.0 / error_t - 1)
        # for every weight in D
        normalize = 0.0
        for i in range(0, len(D)):
            y_i = 1 if training_data[:, 58][i] == 1 else -1
            h_t_i = 1 if h_t[i] == 1 else -1
            D[i] = D[i] * math.exp(-1.0 * alpha * y_i * h_t_i)
            normalize += D[i]

        D = D / normalize

def calculate_error(D, predict_y, y):
    error = 0.0
    for i in range(0, len(y)):
        term = 1 if predict_y[i] != y[i] else 0
        error += D[i] * term
    return error

if __name__ == '__main__':
    main()
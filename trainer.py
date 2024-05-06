'''KYLE MULLEN - CSEC 759 - 5/5/2024
Gathers statistics and class data about each tested item - with class items coming from 'data' folder but being referencable here: 
https://docs.google.com/spreadsheets/d/1FN7WbGfT-mYSDNhvDipuN1vw0OPn_gj7x3jHcNMBog0/edit?usp=sharing
Then operates a logistic regression on the items and outputs a report on the accuracy obtained'''

import numpy
import openandcheck
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, precision_score, f1_score, recall_score


def main():

    # creates 2 lists, one of tuples representing each .asm file, and one of the assigned class for that file
    tuples = []
    classes = []
    with open('C:/Users/smoov/OneDrive - rit.edu/attemptatml/classes.csv', 'r') as thecsv:
        classlist = csv.reader(thecsv)
        for i in range(11, 406):
            tuples.append(openandcheck.check(str(i)))
            thenext = classlist.__next__()
            classes.append(thenext[1])
    
    # Turns these tuples into NumPy arrays
    X = numpy.array(tuples)
    Y = numpy.array(classes)

    # Separates out 10% of the field for testing
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=22) #To vary the results, remove random_state parameter

    # Builds and trains the logistic regression model
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    # Evaluates the model
    y_pred = model.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # precision_weighted = precision_score(y_test, y_pred, average='weighted')
    # recall_weighted = recall_score(y_test, y_pred, average='weighted')
    # f1_weighted = f1_score(y_test, y_pred, average='weighted')
    # print(f"Accuracy: {accuracy}")
    # print(f"Precision: {precision_weighted}")
    # print(f"Recall: {recall_weighted}")
    # print(f"F1: {f1_weighted}")
    report = classification_report(y_test, y_pred, zero_division=1.0)
    print(report)


main()
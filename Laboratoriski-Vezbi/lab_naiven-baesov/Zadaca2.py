import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from sklearn.naive_bayes import CategoricalNB, GaussianNB
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
# Vashiot kod tuka
    train_data = dataset[:int(len(dataset)*0.85)]
    test_data = dataset[int(len(dataset)*0.85):]
    data = dataset[int(len(dataset)*0.30):int(len(dataset)*0.50)]
    train_X = [row[:-1] for row in train_data]
    train_X = [[float(el) for el in element] for element in train_X]
    train_Y = [float(row[-1]) for row in train_data]

    test_X = [row[:-1] for row in test_data]
    test_X = [[float(el) for el in element] for element in test_X]
    test_Y = [float(row[-1]) for row in test_data]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)
    acc=0
    for t_x, true_class in zip(test_X, test_Y):
        pred = classifier.predict([t_x])[0]
        if pred == true_class:
            acc += 1
    print(acc/len(test_data))
    input_data = input()
    input_data = input_data.split(' ')
    input_data = [float(element) for element in input_data]
    pred_data = classifier.predict([input_data])[0]
    print(int(pred_data))
    prob = classifier.predict_proba([input_data])
    print(prob)
# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

# submit na klasifikatorot
    submit_classifier(classifier)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *

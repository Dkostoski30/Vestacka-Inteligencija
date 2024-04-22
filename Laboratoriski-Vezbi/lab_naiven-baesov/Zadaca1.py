import os
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
from submission_script import *
from dataset_script import dataset
os.environ['OPENBLAS_NUM_THREADS'] = '1'


# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
# Vashiot kod tuka
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_data = dataset[:int(len(dataset) * 0.75)]
    train_data_x = [row[:-1] for row in train_data]
    train_data_y = [row[-1] for row in train_data]

    test_data = dataset[int(len(dataset) * 0.75):]
    test_data_x = [row[:-1] for row in test_data]
    test_data_y = [row[-1] for row in test_data]

    classifier = CategoricalNB()
    enc_train_data_x = encoder.transform(train_data_x)
    enc_test_data_x = encoder.transform(test_data_x)

    classifier.fit(enc_train_data_x, train_data_y)
    acc = 0
    for test_x, true_class in zip(enc_test_data_x, test_data_y):
        pred = classifier.predict([test_x])[0]
        if pred == true_class:
            acc += 1

    acc = acc / len(test_data)
    print(acc)
    input_data = input()
    input_data = input_data.split(' ')
    enc_input_data = encoder.transform([input_data])
    pred_class = classifier.predict(enc_input_data)[0]
    prob = classifier.predict_proba(enc_input_data)
    print(pred_class)
    print(prob)

    # submit na trenirachkoto mnozestvo
    train_X = enc_train_data_x
    train_Y = train_data_y
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    test_X = enc_test_data_x
    test_Y = test_data_y
    submit_test_data(test_X, test_Y)
    #
    # # submit na klasifikatorot
    submit_classifier(classifier)
    #
    # # submit na encoderot
    submit_encoder(encoder)
    #
    # # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *

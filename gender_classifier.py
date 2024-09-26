import random
from nltk.corpus import names
import nltk


def gender_features(word):
    return {
        'last_letter': word[-1],
        # 'length': len(word),
        # 'first_letter': word[0],
        'ending_with_hy': str(word[-2:]).lower() == 'hy'
    }


# preparing a list of examples and corresponding class labels.
labeled_names = ([(name, 'male') for name in names.words('input/male.txt')] +
                 [(name, 'female') for name in names.words('input/female.txt')])

random.shuffle(labeled_names)

# we use the feature extractor to process the names data.
featuresets = [(gender_features(n), gender)
               for (n, gender) in labeled_names]

# for gender in ['male', 'female']:
#     count = len(
#         [(x, g) for (x, g) in featuresets if x['last_letter'] == 'y' and g == gender])
#     print(f'Number of {gender} names ending with y = ' + str(count))

# print(featuresets)

# Divide the resulting list of feature
# sets into a training set and a test set.
train_set, test_set = featuresets[500:], featuresets[:500]

# The training set is used to
# train a new "naive Bayes" classifier.
classifier = nltk.NaiveBayesClassifier.train(train_set)

inputName = input("Enter a name: ")

print(classifier.classify(gender_features(inputName)))

# output should be 'male'
print(nltk.classify.accuracy(classifier, train_set))

# it shows accuracy of our classifier and
# train_set. which must be more than 99 %
classifier.show_most_informative_features(50)

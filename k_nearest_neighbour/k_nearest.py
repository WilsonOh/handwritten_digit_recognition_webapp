from k_nearest_neighbour.classes import Test, Neighbour
import k_nearest_neighbour.digits as digits

K = 5

train_file = './inputs/train60000.in'
training = digits.initialise_training_samples(Neighbour, train_file)


def init(test_digit):
    test_sample = digits.initialise_testing_sample(Test, test_digit)
    print("Analyzing digit...")
    digit = digits.find_most_common(training, test_sample, K)
    print(f"My guess is: {digit}")
    return digit

# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
if __name__ == "__main__":
    predictions = []
    for i in range(500):
        predictions.append("London")
    all, good = utils.evaluate_places("birth_dev.tsv", predictions)
    print("num of good:", good)
    print("total amount", all)
    print("percentage:", 100 * good/all)
# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The rules are not mutually exclusive because more than one rule can apply to a single case. For example, a single homeowner would trigger both Rule 1 and Rule 2."
    answers["(b) explain"] = "The rule set is not exhaustive because there are possible attribute combinations not covered by the rules. For instance, a married homeowner with a medium income and employment status is not addressed."
    answers["(c) explain"] = "Ordering is needed because the rules are not mutually exclusive, and applying them in different sequences can affect the classification outcome."
    answers["(d) explain"] = "A default class is needed for any instances that don't match any of the provided rules, to ensure a complete classification coverage."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "To guarantee that the rules don't overlap, each one must classify distinctly different groups based on unique attribute combinations. They seem to be exclusive in how they differentiate between groups like birds, fish, mammals, and reptiles."
    answers["(b) example"] = "The rules do not include a category for amphibians; hence, an organism like a salamander would remain unclassified. This suggests that the rule set does not cover all possibilities within the dataset, as it lacks a classification for each type of vertebrate."
    answers["(c) example"] = "Since every rule pertains to a distinct group and there's no intersection between them, the order of application doesn't affect the outcome of the classification. Therefore, the ordering of the rules is not a concern."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "In back-propagation, the gradient for weights in layer k+1 is calculated using the gradient of weights in layer k via the chain rule."
    answers["(b) explain"] = "The activations at the k+1th layer are computed using the activations from the kth layer, as each layer feeds into the next."
    answers["(c) explain"] = "The vanishing gradient issue leads to minimal updates in a network's early layers, impeding learning. If training errors are nil but test errors are high, it points to overfitting, not vanishing gradients."
    answers["(d) explain"] = "Even if the ANN model perfectly classifies all training instances, the gradients of loss with respect to the weights will be close to zero, not exactly zero, as the learning process typically stops based on a convergence threshold, not an exact zero loss."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5  
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "Choosing k=5 strikes a balance by taking into account several nearest neighbors, which reduces the influence of noise and atypical data points. This choice is less prone to random variations than k=1, and it preserves local data patterns better than higher k values like 50, which might over-generalize."
    answers["(b) explain"] = "In scenarios where classes significantly intersect, opting for a higher K value can be beneficial. This approach lessens the dependence on nearest neighbors, which might not be reliable indicators due to the overlap. A higher K value helps in forming a more consistent decision boundary in these mixed areas."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "The probability of P(A=1|+) at 0.6 demonstrates the frequency of A's occurrence under positive conditions, suggesting a more pronounced connection to positive outcomes than negative ones."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0 
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # string, '+' or '-'
    answers["(b) class label"]= '+'
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'No'
    

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "Given that the equality does not hold here (0.2 ≠ 0.24), it suggests that A and B exhibit a certain level of dependence under the condition of being positive."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)

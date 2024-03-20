# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "yes"
    answers["(c)"] = "yes"
    answers["(d)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The person is classified as a defaulted borrower (DB = Yes) because they are a home owner, which matches Rule 1."
    answers["(b) explain"] = "The person is classified as a defaulted borrower (DB = Yes) because they are single, which matches Rule 2."
    answers["(c) explain"] = "The person is classified as a defaulted borrower (DB = Yes) because they have a low annual income, which matches Rule 3."
    answers["(d) explain"] = "The person's employment status is not directly mentioned in the rules to infer default, but since they are employed, Rule 4 does not apply, and they are still a defaulted borrower based on other attributes."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "yes"
    answers["(c)"] = "yes"
    answers["(d)"] = "no"

    # explain_string: explanation in english prose
    answers["(a) explain"] = "No, the rules are not mutually exclusive because more than one rule can apply to a vertebrate. For example, a bat is warm-blooded and does not give birth, which could classify it as a mammal and also as a bird."
    answers["(b) explain"] = "Yes, the rules are exhaustive for the provided data, as they cover all combinations of the attributes for classification."
    answers["(c) explain"] = "Yes, ordering is needed to prevent misclassification, such as the need to apply the rule for mammals before the rule for birds to classify a bat correctly."
    answers["(d) explain"] = "No, a default class is not necessary for the provided data since the rules are exhaustive. However, it could be considered for any future data where vertebrates may not fit the current rules."

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "yes"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "could be classified as both a mammal (by R3) and a reptile (by R4), showing the rules are not mutually exclusive."
    answers["(b) example"] = "such as a human who is warm-blooded and is therefore classified as a mammal by R3."
    answers["(c) example"] = "If R4 is applied before R3, a warm-blooded animal that does not give birth and is not an aerial."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
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

# -----------------------------------------------------------
def question8():
    answers = {}


    # float
    answers["(a) P(X_1 = 1 | +)"] = None
    answers["(a) P(X_1 = 1 | -)"] = None
    answers["(a) P(X_2 = 1 | +)"] = None
    answers["(a) P(X_2 = 1 | -)"] = None
    answers["(a) P(X_3 = 1 | +)"] = None
    answers["(a) P(X_3 = 1 | -)"] = None

    # string
    answers["(b) label"] = None

    # float
    answers["(c) P(X_1=1)"] = None
    answers["(c) P(X_2=1)"] = None
    answers["(c) P(X_1=1,X_2=1)"] = None

    # string: "dependent" or "independent"
    answers["(c) Relationship between X_1 and X_2"] = None

    # float
    answers["(d) P(A=1)"] = None
    answers["(e) P(X_1=1, X_2=1|Class=+)"] = None
    answers["(e) P(X_1=1|Class=+)"] = None
    answers["(e) P(X_2=1|Class=+)"] = None

    # string: "yes" or "no"
    answers["(e) A and B conditionally independent?"] = None

    # float
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = None
    answers["(b) K"] = None

    # explain_string
    answers["(a) explain"] = None
    answers["(b) explain"] = None

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = None
    answers["(a) P(B=1|+)"] = None
    answers["(a) P(C=1|+)"] = None
    answers["(a) P(A=1|-)"] = None
    answers["(a) P(B=1|-)"] = None
    answers["(a) P(C=1|-)"] = None

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None  # WRONG
    answers["(b) P(R|+)"] = None
    answers["(b) P(R|-)"] = None

    # string, '+' or '-'
    answers["(b) class label"] = None

    # explain_string
    answers["(b) Explain your reasoning"] = None
  
    # float
    answers["(c) P(A=1)"] = None
    answers["(c) P(B=1)"] = None
    answers["(c) P(A=1,B=1)"] = None

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = None
  
    # type: float
    answers["(d) P(A=1)"] = None
    answers["(d) P(B=0)"] = None
    answers["(d) P(A=1,B=0)"] = None

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
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

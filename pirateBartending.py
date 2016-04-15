import random

questions = {
    "strong": "Do ye like yer drinks strong like a whale?",
    "salty": "Do ye like it as salty as the ocean's salty?",
    "bitter": "Would ye like it bitter?",
    "sweet": "Sweet as am apple from the tree of eden?",
    "fruity": "Would ye like a fruity finisher?"
    }

ingredients = {
    "strong": ["good ole rum", "slug of whiskey", "splash of gin"],
    "salty": ["ocean salt", "olive on a stick", "bacon bits"],
    "bitter": ["slice lemon peel", "shake of bitters", "splash of tonic"],
    "sweet": ["sprinkle of sugar", "mouthful of honey", "splash of rootbeer"],
    "fruity": ["slice of orange", "sweet with cherry", "hint of peach"]
    }

def customer_drink():
    answers = {}
    for category in questions:
        question = questions[category]
        correct_check = True
        while correct_check:
            user_answer = input(question)
            user_answer = user_answer.lower()
            if user_answer == "yes" or user_answer == "y":
                answers[category] = user_answer
                correct_check = False
            elif user_answer == "no" or user_answer == "n":
                answers[category] = user_answer
                correct_check = False
            else:
                print("Wrong input!")
    return answers

def make_drink(answers):
    drink = []
    for ingredient_type in ingredients:
        if answers == "yes" or "y":
            drink.append(random.choice(ingredients[ingredient_type]))
        else:
            continue
    return drink

def main():
    answers = customer_drink()
    personal_drink = make_drink(answers)
    print("Your preferred drink has been made!")
    print("Your drink is made with: ")
    for ingredients in personal_drink:
        print("A {}".format(ingredients))

if __name__ == "__main__":
    main()


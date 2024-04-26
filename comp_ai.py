import random


def computer_answer(level, question):

    if level == 'easy':
        if random.random() < 0.5:
            return question['correct_answer']
        else:
            return random.choice([ans for ans in question['answers'] if ans != question['correct_answer']])
    elif level == 'medium':
        if random.random() < 0.7:
            return question['correct_answer']
        else:
            return random.choice([ans for ans in question['answers'] if ans != question['correct_answer']])
    elif level == 'hard':
        if random.random() < 0.95:
            return question['correct_answer']
        else:

            return random.choice([ans for ans in question['answers'] if ans != question['correct_answer']])


def computer_category(categories):
    return random.choice(categories)
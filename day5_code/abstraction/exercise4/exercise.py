from httplib2.auth import quoted_string

alphabet = [
    "a", "b", "c", "d", "e", "f",
    "g", "h", "i", "j", "k"
]

class SingleChoiceQuestion:
    """
    Question for questionnaer

    :param: question_text: string
    :param: list_of_answers: list of strings
    """
    def __init__(self, question_text, list_of_answers):
        if not isinstance(question_text, str):
            raise ValueError("Question must be a string!")
        if not isinstance(list_of_answers, (tuple, list)):
            raise ValueError("Answers must be a tuple or list!")

        self.question_text = question_text
        self.list_of_answers = list_of_answers
        self.letter_to_answer = self.build_letter_to_answer()

    def build_letter_to_answer(self):
        """
        Helper to create dictionary from latin alphabet and provided answers
        :returns: dict
        """
        letter_to_answer = {}
        counter = 0
        for answer in self.list_of_answers:
            letter_to_answer[alphabet[counter]] = answer
            counter += 1
        return letter_to_answer

    def ask(self):
        print(self.question_text)

        for letter, answer in self.letter_to_answer.items():
            print(f"{letter}) {answer}")

        while True:
            users_choice = input("Please pick and answer using the letters: ")
            if users_choice in list(self.letter_to_answer.keys()):
                print()
                return self.letter_to_answer[users_choice]
            else:
                print("Invalid answer!")



class Questionnaire:
    def __init__(self, title):
        self.title = title
        self.questions = []

    # question je datovy typ SingleChoiceQuestion
    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        user_results = {}
        print(self.title, end="\n\n")
        for counter, question in enumerate(self.questions):
            user_answer = question.ask()
            print("Thank you!")
            user_results[counter] = user_answer
        return user_results

    @staticmethod
    def print_out_questions(questions):
        for counter, question in enumerate(questions):
            print(f"Question number: {counter} ====> {question}")


questionnaire = Questionnaire('Laptop satisfaction questionnaire')

q1 = SingleChoiceQuestion('Size of screen', ['less than 15 inches', 'from 15 to 17 inches', 'more than 17 inches'])
q2 = SingleChoiceQuestion('Type of screen', ['matte', 'glossy'])

questionnaire.add_question(q1)
questionnaire.add_question(q2)

questionnaire.print_out_questions([q1, q2])




#answers = questionnaire.run()
#print(f"User answers: {answers}")




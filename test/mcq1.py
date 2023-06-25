'''This module ties together the
questions generation and incorrect answer
generation modules
'''
from question_extraction import QuestionExtractor
from incorrect_answer_generation import IncorrectAnswerGenerator
import re
from nltk import sent_tokenize


class QuestionGeneration:
    '''This class contains the method
    to generate questions
    '''

    def __init__(self, num_questions, num_options):
        self.num_questions = num_questions
        self.num_options = num_options
        self.question_extractor = QuestionExtractor(num_questions)

    def clean_text(self, text):
        text = text.replace('\n', ' ')  # remove newline chars
        sentences = sent_tokenize(text)
        cleaned_text = ""
        for sentence in sentences:
            # remove non alphanumeric chars
            cleaned_sentence = re.sub(r'([^\s\w]|_)+', '', sentence)

            # substitute multiple spaces with single space
            cleaned_sentence = re.sub(' +', ' ', cleaned_sentence)
            cleaned_text += cleaned_sentence

            if cleaned_text[-1] == ' ':
                cleaned_text[-1] = '.'
            else:
                cleaned_text += '.'

            cleaned_text += ' '  # pad with space at end
        return cleaned_text

    def generate_questions_dict(self, document):
        document = self.clean_text(document)
        self.questions_dict = self.question_extractor.get_questions_dict(
            document)
        self.incorrect_answer_generator = IncorrectAnswerGenerator(document)

        for i in range(1, self.num_questions + 1):
            if i not in self.questions_dict:
                continue
            self.questions_dict[i]["options"] \
                = self.incorrect_answer_generator.get_all_options_dict(
                self.questions_dict[i]["answer"],
                self.num_options
            )

        return self.questions_dict
    
a = QuestionGeneration(5,4)
print(a.generate_questions_dict("""
                           Elon Musk has shown again he can influence the digital currency market with just his tweets. After saying that his electric vehicle-making company Tesla will not accept payments in Bitcoin because of environmental concerns, he tweeted that he was working with developers of Dogecoin to improve system transaction efficiency. 

Following the two distinct statements from him, the world's largest cryptocurrency hit a two-month low, while Dogecoin rallied by about 20 percent. The SpaceX CEO has in recent months often tweeted in support of Dogecoin, but rarely for Bitcoin.  In a recent tweet, Musk put out a statement from Tesla that it was concerned about the rapidly increasing use of fossil fuels for Bitcoin (price in India) mining and transaction, and hence was suspending vehicle purchases using the cryptocurrency.  

A day later he again tweeted saying, To be clear, I strongly believe in crypto, but it can't drive a massive increase in fossil fuel use, especially coal. It triggered a downward spiral for Bitcoin value but the cryptocurrency has stabilised since.  A number of Twitter users welcomed Musk's statement. One of them said it's time people started realising that Dogecoin is here to stay and another referred to Musk's previous assertion that crypto could become the world's future currency.
"""))
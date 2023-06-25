import spacy

def generate_questions(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    questions = []
    for sentence in doc.sents:
        sentence_text = sentence.text.strip()
        question = sentence_text.replace(sentence_text, "______")
        answer = sentence_text
        questions.append((question, answer))

    return questions

# Example usage
text = "Python is a popular programming language for data analysis and machine learning. It is widely used in various industries."
questions_with_answers = generate_questions(text)
for question, answer in questions_with_answers:
    print("Question:", question)
    print("Answer:", answer)
    print()

import spacy

def generate_questions_with_answers(text, keyword):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    questions = []
    for sentence in doc.sents:
        sentence_text = sentence.text.strip()
        if keyword.lower() in sentence_text.lower():
            question = sentence_text.replace(keyword, "______")
            answer = keyword
            questions.append((question, answer))

    return questions

# Example usage
text = "Python is a popular programming language for data analysis and machine learning. It is widely used in various industries."
keyword = "Python"
questions_with_answers = generate_questions_with_answers(text, keyword)
for question, answer in questions_with_answers:
    print("Question:", question)
    print("Answer:", answer)
    print()

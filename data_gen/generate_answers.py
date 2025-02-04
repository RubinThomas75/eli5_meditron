import openai
import json
import time
import os

openai.api_key = ""

def generate_eli5_answer(question):
    prompt = f"Explain like I'm five: {question}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def main():
    INPUT_FILE = "eli5_medical_questions_cleaned.json"
    OUTPUT_FILE = "eli5_medical_qa.json"

    with open(INPUT_FILE, "r") as f:
        questions = json.load(f)

    qa_pairs = []
    for i, question in enumerate(questions):
        try:
            answer = generate_eli5_answer(question)
            qa_pairs.append({"question": question, "eli5_answer": answer})
            print(f"Answered {i+1}/{len(questions)}: {question}")
            time.sleep(1)
        except Exception as e:
            time.sleep(10)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(qa_pairs, f, indent=4)

if __name__ == "__main__":
    main()

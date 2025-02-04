import openai
import json
import time
import os

openai.api_key = ""

TOTAL_QUESTIONS = 2000
BATCH_SIZE = 50
OUTPUT_FILE = "eli5_medical_questions.json"

def generate_questions(batch_size):
    prompt = (
        f"Generate {batch_size} UNIQUE medical questions a child might ask. "
        "Cover different topics like the brain, heart, skin, digestion, breathing, and common illnesses."
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )

    return response.choices[0].message.content.strip().split("\n")

def generate_medical_questions():
    questions = set() 

    while len(questions) < TOTAL_QUESTIONS:
        try:
            new_questions = generate_questions(BATCH_SIZE)
            for q in new_questions:
                if q and q not in questions:
                    questions.add(q)

            print(f"Generated {len(questions)} unique questions so far...")
            time.sleep(1)

        except Exception as e:
            print(f"Error: {e}. Retrying after 10 seconds...")
            time.sleep(10)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(list(questions), f, indent=4)

    print(f"Generated {len(questions)} questions and saved them to '{OUTPUT_FILE}'!")

def main():
    generate_medical_questions()

if __name__ == "__main__":
    main()
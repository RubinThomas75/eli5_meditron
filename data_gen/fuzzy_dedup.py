import json
from rapidfuzz import fuzz

INPUT_FILE = "eli5_medical_questions.json"
OUTPUT_FILE = "eli5_medical_questions_cleaned.json"

with open(INPUT_FILE, "r") as f:
    questions = json.load(f)

SIMILARITY_THRESHOLD = 85

def is_duplicate(new_question, existing_questions, threshold=SIMILARITY_THRESHOLD):
    """Check if a new question is a near-duplicate of any existing question."""
    for existing in existing_questions:
        if fuzz.ratio(new_question.lower(), existing.lower()) > threshold:
            return True
    return False

unique_questions = []
for question in questions:
    if not is_duplicate(question, unique_questions):
        unique_questions.append(question)


with open(OUTPUT_FILE, "w") as f:
    json.dump(unique_questions, f, indent=4)


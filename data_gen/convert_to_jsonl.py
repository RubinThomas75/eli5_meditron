import json

TRAIN_INPUT = "eli5_medical_train.json"
VAL_INPUT = "eli5_medical_val.json"
TRAIN_OUTPUT = "eli5_medical_train.jsonl"
VAL_OUTPUT = "eli5_medical_val.jsonl"

SYSTEM_MESSAGE = "[SYSTEM]: You are a helpful medical assistant who explains complex topics in simple terms."

def format_chat_messages(question, answer):
    return f"{SYSTEM_MESSAGE}\n[USER]: {question}\n[ASSISTANT]: {answer}"

def convert_json_to_jsonl(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    with open(output_file, "w") as f:
        for item in data:
            formatted_text = format_chat_messages(item["question"], item["eli5_answer"])
            json.dump({"text": formatted_text}, f)
            f.write("\n")

def main():
    convert_json_to_jsonl(TRAIN_INPUT, TRAIN_OUTPUT)
    convert_json_to_jsonl(VAL_INPUT, VAL_OUTPUT)
    print("Conversion completed")
if __name__ == "__main__":
    main()

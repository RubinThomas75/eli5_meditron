import json
import random

INPUT_FILE = "eli5_medical_qa.json"
TRAIN_FILE = "eli5_medical_train.json"
VALIDATION_FILE = "eli5_medical_val.json"
TEST_FILE = "eli5_medical_test.json"

TEST_SIZE = 20
TRAIN_RATIO = 0.8

def load_data(filename):
    """Load JSON data from a file."""
    with open(filename, "r") as f:
        return json.load(f)


def save_data(data, filename):
    """Save JSON data to a file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def split_dataset(data):
    random.shuffle(data)

    test_set = data[:TEST_SIZE]
    remaining_data = data[TEST_SIZE:]

    split_index = int(TRAIN_RATIO * len(remaining_data))
    train_set = remaining_data[:split_index]
    val_set = remaining_data[split_index:]

    return train_set, val_set, test_set

def main():
    data = load_data(INPUT_FILE)
    train_set, val_set, test_set = split_dataset(data)
    save_data(train_set, TRAIN_FILE)
    save_data(val_set, VALIDATION_FILE)
    save_data(test_set, TEST_FILE)

    print(f"Training set: {len(train_set)} questions")
    print(f"Validation set: {len(val_set)} questions")
    print(f"Test set: {len(test_set)} questions (fixed at {TEST_SIZE})")

if __name__ == "__main__":
    main()

import csv
import json
import string
import random


def prepare_csv_file(file_object, response):
    file_content = file_object.read()
    if isinstance(file_content, bytes):
        file_content = file_content.decode('utf-8')
    json_data = json.loads(file_content)

    unique_meta_keys = set()
    for item in json_data:
        meta_data = item.get("meta", {})
        unique_meta_keys.update(meta_data.keys())

    writer = csv.writer(response)

    header_row = ["Table Name"] + list(unique_meta_keys)
    writer.writerow(header_row)

    for item in json_data:
        table_name = item.get("table")
        meta_data = item.get("meta", {})

        meta_values = [table_name] + [
            meta_data.get(key, "") for key in unique_meta_keys
        ]
        writer.writerow(meta_values)


def generate_n_length_random_string(
    n: int,
    use_uppercase: bool = True,
    use_lowercase: bool = False,
    use_digits: bool = False,
    use_whitespace: bool = False,
    use_punctuation: bool = False,
    use_hex: bool = False,
    custom_characters: str = None,
) -> str:

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_whitespace:
        characters += string.whitespace
    if use_punctuation:
        characters += string.punctuation
    if use_hex:
        characters += string.hexdigits
    if use_digits:
        characters += string.digits
    if custom_characters:
        characters += custom_characters

    return "".join(random.choices(characters, k=n))
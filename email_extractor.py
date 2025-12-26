# Email Extractor

import re

input_file = "input.txt"
output_file = "emails.txt"

with open(input_file, "r") as file:
    content = file.read()

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content)

with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed.")
print(f"Total emails found: {len(emails)}")
print("Saved to emails.txt")
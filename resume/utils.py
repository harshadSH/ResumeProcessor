import re
from pdfminer.high_level import extract_text  # Example: For extracting PDF text

def parse_resume(file):
    # Read the content of the uploaded file
    text = extract_text(file)

    # Regular expression for finding email
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = re.findall(email_pattern, text)

    # Regular expression for finding phone numbers
    phone_pattern = r'\+?\d{1,3}[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}'
    phone_numbers = re.findall(phone_pattern, text)

    # Splitting text to get first name (assuming it's the first word in the document)
    lines = text.split('\n')
    first_name = lines[0].strip() if lines else "Unknown"

    return {
        "first_name": first_name.split()[0] if first_name else "Unknown",
        "email": email[0] if email else "Not Found",
        "mobile_number": phone_numbers[0] if phone_numbers else "Not Found",
    }

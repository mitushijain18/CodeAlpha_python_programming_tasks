import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            # Regex pattern to find email addresses
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            emails = re.findall(email_pattern, content)
        
        with open(output_file, 'w') as file:
            for email in emails:
                file.write(email + '\n')
        
        print(f"Success! Extracted {len(emails)} emails to {output_file}")
    except FileNotFoundError:
        print("Error: The input file was not found.")

if __name__ == "__main__":
    extract_emails('data.txt', 'emails.txt')
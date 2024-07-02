# Read the requirements.txt file
with open('requirements.txt', 'r') as file:
    lines = file.readlines()

# Filter out lines containing '@ file://'
cleaned_lines = [line for line in lines if '@ file://' not in line]

# Write the cleaned lines back to the file
with open('requirements_cleaned.txt', 'w') as file:
    file.writelines(cleaned_lines)

print("Cleaned requirements saved to requirements_cleaned.txt")

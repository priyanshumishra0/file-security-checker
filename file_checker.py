import os

file_name = input("Enter the file name: ")

print("Your file name is:", file_name)

if os.path.exists(file_name):
    print("File found")

    size = os.path.getsize(file_name)
    print("File size:", size, "bytes")

    extension = os.path.splitext(file_name)[1].lower()
    print("File type:", extension)

    suspicious_extensions = [".exe", ".bat", ".cmd", ".scr", ".vbs"]

    if extension in suspicious_extensions:
        print("Warning: This file type can execute commands")
    else:
        print("File type looks normal")

    suspicious_words = ["virus", "malware", "trojan", "ransomware"]

    try:
        with open(file_name, "r", errors="ignore") as file:
            content = file.read().lower()

        found_words = []

        for word in suspicious_words:
            if word in content:
                found_words.append(word)

        if found_words:
            print("Warning: Suspicious words found:", found_words)
        else:
            print("No suspicious words found")

    except Exception:
        print("Could not read file content")

else:
    print("File not found")
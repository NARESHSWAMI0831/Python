# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


# Daily Python Practice - July 25

# A list of programming languages
languages = ["Python", "Java", "C++", "JavaScript", "Go"]

# Print each language with a number
print("Programming Languages:")
for i, lang in enumerate(languages, start=1):
    print(f"{i}. {lang}")

# Add a new language
languages.append("Rust")
print("\nUpdated List:", languages)

# Remove a language
languages.remove("Java")
print("After Removing Java:", languages)



# Daily Python Practice - July 26

# Writing to a file
with open("my_notes.txt", "w") as file:
    file.write("This is my first note written using Python.\n")
    file.write("File handling is easy and useful!\n")

# Reading from the same file
with open("my_notes.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

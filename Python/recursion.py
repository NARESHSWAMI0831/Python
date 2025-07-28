# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

# Daily Python Practice - July 28

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

# Sample tests
words = ["Radar", "Python", "Madam", "Level", "Coding"]

for word in words:
    if is_palindrome(word):
        print(f"✅ '{word}' is a palindrome")
    else:
        print(f"❌ '{word}' is not a palindrome")


from collections import deque

def is_palindrome(text):
    """
    Checks if a string is a palindrome using deque.

    Parameters:
        text(str): String to check for palindrome

    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    # normalize text: remove spaces and convert to lowercase
    normalized_text = ''.join(text.lower().split())
    
    # empty string is a palindrome
    if not normalized_text:
        return True
    
    # add all characters to deque
    char_deque = deque(normalized_text)
    
    # compare characters from both ends
    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        
        if left_char != right_char:
            return False
    
    return True


if __name__ == "__main__":
    # test cases
    test_strings = [
        "radar",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "Hello World",
        "Madam",
        "Step on no pets",
        "Python",
        "А роза упала на лапу Азора"
    ]
    
    print("=" * 50)
    print("Palindrome Checker")
    print("=" * 50)
    
    for test in test_strings:
        result = is_palindrome(test)
        status = "Palindrome" if result else "Not a palindrome"
        print(f"'{test}' -> {status}")
    
    print("=" * 50)
from importlib import import_module


log = import_module("utils", "..").log


@log()
def isValid(s: str) -> bool:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    
    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Note that an empty string is also considered valid.

    Example:
    Input: "()"
    Output: true
    
    Input: "()[]{}"
    Output: true
    
    Input: "(]"
    Output: false
    
    Input: "([)]"
    Output: false
    
    Input: "{[]}"
    Output: true
    
    :param s: str - the string to check if it is valid
    :return: bool - True if the string is valid, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack: list = []
    brace_resolver: dict = {
        ')': "(",
        ']': "[",
        '}': "{"
    }
    opening_braces: list = ["(", "[", "{"]
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        elif char in opening_braces:
            stack.append(char)
        elif stack[-1] == brace_resolver[char]:
            stack.pop()
        else:
            return False
    return True if len(stack) == 0 else False


def run():
    isValid(s="()")
    isValid(s="()[]{}")
    isValid(s="(]")
    isValid(s="([)]")
    isValid(s="{[]}")
    isValid(s="")

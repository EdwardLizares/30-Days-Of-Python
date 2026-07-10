import re
def is_valid_variable(s):
    regex_pattern = r'^\d|-'
    return not bool(re.search(regex_pattern, s))

if __name__ == "__main__":
    print(is_valid_variable("abs-1"))

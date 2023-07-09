import re

def regex_query_tool():
    while True:
        print("Regex Query Tool")
        print("Enter 'q' to quit")
        text = input("Enter the text to search: ")
        if text == 'q':
            break

        pattern = input("Enter the regular expression pattern: ")
        if pattern == 'q':
            break

        try:
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            if len(matches) > 0:
                print("Matches found:")
                for match in matches:
                    print(match)
            else:
                print("No matches found.")
        except re.error as e:
            print("Invalid regex pattern:", e)

        print()

#Example usage
regex_query_tool()
def append_after(filename="", search_string="", new_string=""):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

    except Exception:
        pass  # You don't need to handle exceptions, so just continue if any occur

# Example usage:
if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

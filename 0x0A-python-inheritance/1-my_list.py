class MyList(list):
    """Custom class MyList that inherits from the list class."""

    def print_sorted(self):
        """Prints the list in ascending order."""

        sorted_list = sorted(self)
        print(sorted_list)

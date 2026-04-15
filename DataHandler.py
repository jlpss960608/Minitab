class DataHandler:
    def __init__(self):
        self.data = []

    def add_numbers(self, numbers):
        self.data.extend(numbers)

    def get_data(self):
        return self.data

    def clear_data(self):
        self.data = []

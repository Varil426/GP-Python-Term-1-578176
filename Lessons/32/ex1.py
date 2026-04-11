"""
Utwórz symulator przeglądarki, gdzie historia przeglądania będzie zapisywana w formie stosu.
Użytkownik może wchodzić na różne strony w programie i cofać się w historii przeglądania.
"""

from Stack import Stack

class BrowserHistory:
    def __init__(self):
        self.history = Stack()
        self.current_page = None

    def go_to_page(self, url):
        self.history.push(self.current_page)
        self.current_page = url

    def go_back(self):
        previous_page = self.history.pop()
        if previous_page is not None:
            self.current_page = previous_page

    def print(self):
        print(f"Current page: {self.current_page}")
        print("History:")
        for page in reversed(self.history.stack):
            print(page)


history = BrowserHistory()

history.go_to_page("www.google.com")
history.go_to_page("giganciprogramowania.pl")
history.go_to_page("giganciprogramowania.pl/startPage")

history.print()

history.go_back()
history.go_back()

history.print()

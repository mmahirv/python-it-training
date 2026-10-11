class Book:
    language = "Turkish"
    
    def __init__(self, title, author, total_page):
        self.title = title
        self.author = author
        self.total_page = total_page
        
    def __str__(self):
        return f'{self.title} -{self.author}- {self.total_page}- {self.language}'
    
    def increase_total_page(self, page):
        self.total_page += page
    
    def decrease_total_page(self, page):
        if self.total_page < page:
            print(f'Page number is {self.total_page} and can not be smaller then zero. Give me smaller number than now:')
        else:
            self.total_page -= page
    
    def change_language(self, new_lang):
        self.language = new_lang
    
first_book = Book('Harry', 'Pother', 500)
second_book = Book('Var misin?', 'Dogan Cuceloglu', 400)

print(first_book,'\n', second_book)

first_book.increase_total_page(300)
second_book.increase_total_page(100)

print(first_book,'\n', second_book)

first_book.decrease_total_page(1000)
second_book.decrease_total_page(100)

print(first_book,'\n', second_book)

first_book.change_language('Nederlands')

print(first_book,'\n', second_book)
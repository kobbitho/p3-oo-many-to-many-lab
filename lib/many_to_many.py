class Author:
    authors = []

    def __init__(self, name):
        self.name = name
        self.authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.contracts_list if isinstance(contract.author, Author) and contract.author == self]

    def books(self):
      return [contract.book for contract in self.contracts() if isinstance(contract.book, Book)]

    def sign_contract(self, book, date, royalties):
        if isinstance(self, Author) and isinstance(book, Book):
            if isinstance(date, str):
                new_contract = Contract(author=self, book=book, date=date, royalties=royalties)
                return new_contract
            
            else:
                raise Exception("Date must be a string")
        else:
            raise Exception("Invalid input. Author and Book must be instances of the Author and Book classes, respectively.")

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total


class Book:
    books = []

    def __init__(self, title):
        self.title = title
        self.books.append(self)
    def contracts(self):
        return [contract for contract in Contract.contracts_list if isinstance(contract.book, Book) and contract.book == self]
    
    def authors(self):
        return[contract.author for contract in self.contracts()]
        


class Contract:
    contracts_list = []

    def __init__(self, author, book, date, royalties):
        if  not isinstance(author, Author) or not isinstance(book, Book):
            raise Exception("Invalid input. Author and Book must be instances of the Author and Book classes, respectively.")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.contracts_list.append(self)
        
        
            

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.contracts_list if isinstance(contract.author, Author) and isinstance(contract.book, Book) and contract.date == date]
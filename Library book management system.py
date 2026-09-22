class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price
        self.category = self._categorize_price(price)

    def _categorize_price(self, price: float) -> str:
        if price >= 1000:
            return "Premium"
        elif 500 <= price < 1000:
            return "Standard"
        else:
            return "Basic"

    def display_info(self):
        print(f"| {self.title:<30} | {self.author:<20} | ₹{self.price:<8.2f} | {self.category:<8} |")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("\n" + "=" * 74)
        print("                      LIBRARY CATALOGUE                         ")
        print("=" * 74)
        print(f"| {'Title':<30} | {'Author':<20} | {'Price':<9} | {'Category':<8} |")
        print("-" * 74)
        for book in self.books:
            book.display_info()
        print("=" * 74)

    @staticmethod
    def climb_stairs(n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == "__main__":
    lib = Library()

    lib.add_book(Book("Introduction to Algorithms", "CLRS", 1250.00))
    lib.add_book(Book("Clean Code", "Robert C. Martin", 750.00))
    lib.add_book(Book("The Pragmatic Programmer", "Andrew Hunt", 450.00))

    lib.display_books()

    stairs = 5
    ways = lib.climb_stairs(stairs)
    print(f"\n[DP] Distinct ways to climb {stairs} stairs (taking 1 or 2 steps): {ways}")
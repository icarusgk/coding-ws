class Book:
  material = 'paper'
  cover = 'paperback'
  all_books = []

print(Book.material)
print(Book.all_books)

my_book = Book()
print(my_book.all_books)

class RockBand:
    genre = 'rock'
    key_instruments = ['electric guitar', 'drums']
    n_members = 4

acdc = RockBand()
print(acdc.genre)
print(acdc.key_instruments)
print(acdc.n_members)


# * Methods
class Ship:
  def __init__(self, name, capacity):
    self.name = name
    self.capacity = capacity
    self.cargo = 1

  def sail(self):
    print(f'{self.name} has sailed!')

  def convert_cargo(self):
    return self.cargo * 1000

  def name_captain(self, cap):
    self.captain = cap
    print(f'{self.captain} is the captain of the {self.name}')

  def free_space(self):
        return self.capacity - self.cargo

  def load_cargo(self, weight):
        if self.cargo + self.free_space():
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

  def unload_cargo(self, weight):
      if self.cargo - weight >= 0:
          self.cargo -= weight
          print("Unloaded {} tons".format(weight))
      else:
          print("Cannot unload that much")
  
  



black_pearl = Ship('Black Pearl', 800)
black_pearl.name_captain('Jack Sparrow')
print(black_pearl.captain)

# example
black_pearl.load_cargo(600)
# "Loaded 600 tons"

black_pearl.unload_cargo(400)
# "Unloaded 400 tons"

black_pearl.load_cargo(700)
# "Cannot load that much"

black_pearl.unload_cargo(300)
# "Cannot unload that much"

class Sun:
    n = 0  # number of instances of this class

    def __new__(cls):
        if cls.n == 0: 
            cls.n += 1
            return object.__new__(cls)  # create new object of the class


class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)

    def __str__(self):
        return "Transaction {} for {} ({})".format(self.number, self.funds, self.status)


payment = Transaction("000001", 9999.999)
print(payment)
# Transaction 000001 for 9999.999 (active)
print(repr(payment))
# Transaction(000001, 9999.999)
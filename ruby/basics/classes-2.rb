# Private and Public
class Person
  def initialize(name, age)
    @name = name
    @age = age
  end

  public    # This method can be called from outside the class.

  def about_me
    puts "I'm #{@name} and I'm #{@age} years old!"
  end

  private   # This method can't!

  def bank_account_number
    @account_number = 12345
    puts "My bank account number is #{@account_number}."
  end
end

eric = Person.new("Eric", 26)
eric.about_me
eric.bank_account_number

# attr_reader and attr_writer
class Person
  attr_reader :job
  attr_writer :job
  def initialize(name, job)
    @name = name
    @job = job
  end
end

# Replace both with attr_accessor

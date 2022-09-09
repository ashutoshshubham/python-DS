class Movie:
    def __init__(self, title,rating,year):
        self.title = title
        self.rating = rating
        self.year = year

    def info(self):
        return (f'{self.title}({self.year}) -> {self.rating}')

    #  > overloaded

    def __gt__(self,other):
        if self.rating > other.rating:
            return True
        else:
            return False

    def __lt__(self,other):
        if self.rating < other .rating:
            return True
        else:
            return False

    def __repr__(self):
        return self.title


m = Movie('Jb tk hai jaan',4.8,2013)
m2 = Movie("Ligar",1,2022)

print(m > m2)
print(m2 > m)

movies = [m,m2]
movies.sort()
print(movies)
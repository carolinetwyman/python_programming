#unordered collection of unique elements that are hashable
hero = 'harry potter'
guide = 'dumbledore'
villain = 'lord v'
characters = {hero, guide, villain}
print(hash(hero))

characters = {hero, guide, villain}
print(characters, "characters")


customers = [("John", 240000),
             ("Alice", 120000),
             ("Ann", 1100000),
             ("Zach", 440000)]

whales = [x for x,y in customers if y>1000000]
print(whales)


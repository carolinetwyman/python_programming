#unordered collection of unique elements that are hashable
hero = 'harry potter'
guide = 'dumbledore'
villain = 'lord v'

characters_set = {hero, guide, villain}
print(characters_set, "characters")
print(hash(hero))
team_1 = [hero, guide]
team_2 = [villain]
teams = [team_1, team_2]
print(teams, "teams list")

characters_list = [hero, guide, villain]
team_3 = [hero, guide]
team_4 = [hero, guide]
print(teams, "teams list")

clone_army = {hero, hero, hero, hero, hero}
print(clone_army, "clone army")

clone_army = [hero, hero, hero, hero]
print(clone_army, "clone army")


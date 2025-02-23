
CHEESES = ["cheddar","gouda", "camembert"]
def roll_call_dwarves(dwarfs):
    i = 1
    for dwarf in dwarfs:
        print(f'{i}. {dwarf}')
        i += 1


def summon_captain_planet(planeteer_calls):
    return  [f'{call.capitalize()}!' for call in planeteer_calls]


def long_planeteer_calls(words):
    if len(words) > 4:
        return False
    return True

def find_the_cheese(foods):
    for food in foods:
        if food in CHEESES:
            return(food)

snacks = ["crackers", "gouda", "thyme"]
find_the_cheese(snacks)
#=> "gouda"

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
find_the_cheese(soup)



roll_call_dwarves(dwarfs = ["Doc", "Dopey", "Bashful", "Grumpy"])

print(summon_captain_planet(planeteer_calls = ["earth", "wind", "fire", "water", "heart"]))

short_words = ["puff", "go", "two"]
print(long_planeteer_calls(short_words))

assorted_words = ["two", "go", "industrious", "bop"]
long_planeteer_calls(assorted_words)


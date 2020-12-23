import re
def read_ingredients(file):
    results = []
    with open(file) as f:
        for line in f.readlines():
            matches = re.match(r'(\D+) \(contains ([\D,]+)\)', line)
            ingredients = list( [ ingredient.strip() for ingredient in matches[1].split(' ') ])
            allergens = list([ allergen.strip() for allergen in matches[2].split(',') ])
            results.append((ingredients, allergens))
    return results

entries = read_ingredients('input.txt')
allergen_lookup = {}
for entry in entries:
    for allergen in entry[1]:
        ingredients_as_set = set(entry[0])
        if allergen in allergen_lookup:
            allergen_lookup[allergen] = set.intersection(allergen_lookup[allergen], ingredients_as_set)
        else:
            allergen_lookup[allergen] = ingredients_as_set

# get all the 1 length answers and remove these from allergen lookup sets
done = False
while not done:
    done = True
    resolved = set([ value for value in allergen_lookup.values() if type(value) != set ])
    updated_allergen_lookup = {}
    for key, ingredients in allergen_lookup.items():
        if type(ingredients) == set:
            candidate_ingredients = ingredients - resolved
            if len(candidate_ingredients) > 1:
                updated_allergen_lookup[ key ] = candidate_ingredients
                done = False
            else:
                updated_allergen_lookup[ key ] = list(candidate_ingredients)[0]
        else:
            updated_allergen_lookup[ key ] = ingredients
        
    allergen_lookup = updated_allergen_lookup

all_ingredient_instances = [ ingredient for entry in entries for ingredient in entry[0] ]
allergenic_ingredients = list(allergen_lookup.values())
part1 = sum([ 1 for ingredient in all_ingredient_instances if ingredient not in allergenic_ingredients ])
print(f"Part1 - {part1}")
keys = list(allergen_lookup.keys())
keys.sort()
part2 = ','.join([ allergen_lookup[key] for key in keys ])
print(f"Part2 - {part2}")

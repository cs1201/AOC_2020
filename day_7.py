import re
from pprint import pprint

def extract_rules(data):
    rules = {}
    for item in data:
        base = re.match(r'(.*?) bags', item).group(1)
        colours = re.findall(r'(\d+) (.+?) bag', item)
        rules[base] = colours
    return rules

def contains_sg(rules, colour):
    if 'shiny gold' in colour:
        return True
    return any(contains_sg(rules, c) for _,c in rules[colour])

def nested_count(rules, colour):
    return sum(int(quantity)*nested_count(rules, colour) for quantity, colour in rules[colour]) + 1 #Add 1 to account for first base

def part_one(rules):
    return (sum(contains_sg(rules, c) for c in rules.keys()) - 1) #Remove shiny gold base

def part_two(rules):
    return nested_count(rules, 'shiny gold') - 1

with open("data/day_7.txt") as f:
    data = [x.strip('.') for x in f.read().split('\n')]
    rules = extract_rules(data)
    print(f"Part One: {part_one(rules)}")
    print(f"Part Two: {part_two(rules)}")
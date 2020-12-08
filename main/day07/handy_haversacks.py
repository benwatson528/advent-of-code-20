import re
from collections import defaultdict
from typing import List


def solve_holders(statements: List[str]) -> int:
    bags = {}
    index = defaultdict(list)
    parse_statements(bags, index, statements)
    return len(find_gold_bag_holders(index)) - 1


def solve_contents(statements: List[str]) -> int:
    bags = {}
    index = defaultdict(list)
    parse_statements(bags, index, statements)
    return find_gold_bag_contents(bags, "shiny gold", 1) - 1


def find_gold_bag_holders(index):
    stack = ["shiny gold"]
    gold_bag_holders = set()
    while stack:
        current_bag = stack.pop()
        gold_bag_holders.add(current_bag)
        if index[current_bag]:
            stack.extend(index[current_bag])
    return gold_bag_holders


def find_gold_bag_contents(bags, current_bag, num_bags):
    total = num_bags
    for child_bag in bags[current_bag]:
        if child_bag != (None, None):
            total += find_gold_bag_contents(bags, child_bag[0], num_bags * child_bag[1])
        else:
            return total
    return total


def parse_statements(bags, index, statements):
    for statement in statements:
        split_statement = statement.split(" contain ")
        parent_bag = re.search(r"(.+?) bags?$", split_statement[0]).group(1)
        child_bags = []
        for child_bag in split_statement[1].split(", "):
            child_bag = parse_child_bag_details(child_bag)
            index[child_bag[0]].append(parent_bag)
            child_bags.append(child_bag)
        bags[parent_bag] = child_bags


def parse_child_bag_details(bag):
    m = re.search(r"^(\d) (.+?) bag[s]?|no other bags.$", bag)
    if not m.group(2):
        return None, None
    return m.group(2), int(m.group(1))

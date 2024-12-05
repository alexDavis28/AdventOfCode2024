import re

with open("input.txt", "r") as file:
    text = file.read()
raw_rules, raw_updates = text.split("\n\n")
rules = [i.split("|") for i in raw_rules.split("\n")]
updates = raw_updates.split("\n")

rules_regex = [fr"({a})(.*?)(?={b})|(^((?!{a}).)*$)|(^((?!{b}).)*$)" for a, b in rules]

valid_updates = []
invalid_updates = []

for update in updates:
    applied_rules = [re.search(rule, update) is not None for rule in rules_regex]
    rule_check = all(applied_rules)
    # print([(update, rule, re.search(rule, update) is not None) for rule in rules_regex])
    # print(rule_check)
    if rule_check:
        valid_updates.append(update.split(","))
    else:
        invalid_updates.append((update.split(","), applied_rules))
middle_values = [int(i[len(i)//2]) for i in valid_updates]
# print(sum(middle_values))

number_regex = r"\d+"


print("fixing invalid updates")
print(invalid_updates)

# jesus christ i am sorry for this solution

for update, applied_rules in invalid_updates:
    for i, rule_check in enumerate(applied_rules):
        if not rule_check:
            rule = rules_regex[i]
            value_to_move = re.findall(number_regex, rule)[0]
            value = update.pop(update.index(value_to_move))
            j = 0
            update.insert(0, value)
            while re.search(rule, ",".join(update)) is None:
                value = update.pop(j)
                j += 1
                if j > len(update):
                    raise ValueError("uh oh")
                    # catch impossible
                update.insert(j, value)

invalid_updates = [",".join(i[0]) for i in invalid_updates]
new_valid_updates = []

while len(invalid_updates) > 0:
    tmp_valid_updates = []
    tmp_invalid_updates = []

    for update in invalid_updates:
        print(update)
        applied_rules = [re.search(rule, update) is not None for rule in rules_regex]
        rule_check = all(applied_rules)
        # print([(update, rule, re.search(rule, update) is not None) for rule in rules_regex])
        # print(rule_check)
        if rule_check:
            tmp_valid_updates.append(update.split(","))
        else:
            tmp_invalid_updates.append((update.split(","), applied_rules))

    number_regex = r"\d+"

    for update, applied_rules in tmp_invalid_updates:
        for i, rule_check in enumerate(applied_rules):
            if not rule_check:
                rule = rules_regex[i]
                value_to_move = re.findall(number_regex, rule)[0]
                value = update.pop(update.index(value_to_move))
                j = 0
                update.insert(0, value)
                while re.search(rule, ",".join(update)) is None:
                    value = update.pop(j)
                    j += 1
                    if j > len(update):
                        raise ValueError("uh oh")
                        # catch impossible
                    update.insert(j, value)
    new_valid_updates += tmp_valid_updates
    invalid_updates = tmp_invalid_updates
    invalid_updates = [",".join(i[0]) for i in invalid_updates]

# print(new_valid_updates)

middle_values = [int(i[len(i)//2]) for i in new_valid_updates]
print(sum(middle_values))
import problem1
def rectfier(rules, update):
    #print("Checking update:", update)
    modified = False  # To track if a swap happens

    for index, page in enumerate(update):
        if page in rules.keys():
            #print(f"Page '{page}' found in rules with dependencies: {rules[page]}")
            for rule in rules[page]:
                if rule in update and rule not in update[:index]:  # Rule violated
                    #print(f"Rule '{rule}' violates order. Swapping '{page}' with '{rule}'")
                    # Perform swap
                    rule_index = update.index(rule)
                    update[index], update[rule_index] = update[rule_index], update[index]
                    #print("Updated list after swap:", update)
                    modified = True
                    break  # Break after one swap to re-evaluate the list
            if modified:
                break  # Break outer loop as well to re-check
    return not modified  # Return True if no modifications were needed

# Main logic
with open('input.txt') as f:
    lines = [line.strip().upper() for line in f]  # Clean and standardize input
    ans = 0
    l = len(lines)
    rules = {}
    updates = []  
    flag = True

    # Parse rules and updates
    for line in lines:
        if line == '':
            flag = False
            continue
        if flag:
            a, b = line.split('|')
            if b not in rules:
                rules[b] = []
            rules[b].append(a)
        else:
            updates.append(line.split(','))

    #print("Parsed Rules:", rules)
    #print("Updates to process:", updates)

    # Process each update
    for update in updates:
        if not problem1.is_valid(rules, update):  # Check if update is valid
            while not rectfier(rules, update):  # Keep swapping until valid
                pass
            ans += int(update[len(update) // 2])  # Add middle element of valid list
    print("Final Answer:", ans)

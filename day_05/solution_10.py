import src, helpers

constraints = []
for rule in src.rules_list:
    before, after = map(int, rule.split('|'))
    constraints.append((before, after))

middle_count = 0
for update_order in src.updates_list:
  mapped_list = list(map(int,update_order.split(",")))
  if not helpers.is_correctly_sorted(constraints, mapped_list):
    correct_list = helpers.fix_the_list(constraints, mapped_list)
    middle_count += mapped_list[int(len(correct_list)/2)]

print(middle_count)
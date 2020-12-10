with open('input', 'r') as fd:
    adapters = sorted(list(map(int, fd.readlines())))

# Final difference is always 3 so we count it here
diff_1, diff_3 = 0, 1
prev_adapter = 0
for adapter in adapters:
    if adapter - prev_adapter == 1:
        diff_1 += 1
    if adapter - prev_adapter == 3:
        diff_3 += 1
    prev_adapter = adapter

print(diff_1 * diff_3)

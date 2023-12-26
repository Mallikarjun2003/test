s = ["3", "30", "34", "5", "9"]
sorted_s = sorted(s, key=lambda x: x * 3, reverse=True)
result = "".join(sorted_s)
print(result)

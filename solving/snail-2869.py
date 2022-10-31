a, b, v = map(int, input().split())
end = (v - b) / (a - b)
print(int(end) if end == int(end) else int(end) + 1)

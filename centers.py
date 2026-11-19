with open("data/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]

donations = [float(line) for line in raw if not line.startswith("#")]
print(len(donations), "values")

n = len(donations)
total = sum(donations)
mean = total / n

print(f"n = {n}, total = {total:.2f}")
print(f"mean = {mean:.2f}")

clean = [d for d in donations if d < 5000]
print(f"mean with    outlier: {sum(donations)/len(donations):.2f}")
print(f"mean without outlier: {sum(clean)/len(clean):.2f}")
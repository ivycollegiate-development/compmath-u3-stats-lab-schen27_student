from collections import Counter

with open("data/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]
donations = [float(line) for line in raw if not line.startswith("#")]

def mean_of(values):
    return sum(values) / len(values)

def median_of(values):
    s = sorted(values)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2

def mode_of(values):
    counts = Counter(values)
    best = counts.most_common(1)[0]
    return best if best[1] > 1 else None

clean = [d for d in donations if d < 5000]

print(f"{'set':<10}{'mean':>12}{'median':>12}")
for label, vals in (("all 200", donations), ("no outlier", clean)):
    print(f"{label:<10}{mean_of(vals):>12.2f}{median_of(vals):>12.2f}")

print("mode of all 200:", mode_of(donations))
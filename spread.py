with open("data/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]

donations = [float(line) for line in raw if not line.startswith("#")]
clean = [d for d in donations if d < 5000]

def mean_of(v):
    return sum(v) / len(v)

def median_of(v):
    s = sorted(v)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

def variance_of(v):
    m = mean_of(v)
    return sum((x - m) ** 2 for x in v) / len(v)

def stdev_of(v):
    return variance_of(v) ** 0.5

clean = [d for d in donations if d < 5000]

print(f"{'set':<12}{'mean':>10}{'median':>10}{'range':>12}{'stdev':>12}")
for label, vals in (("all 200", donations), ("clean 199", clean)):
    print(f"{label:<12}{mean_of(vals):>10.2f}{median_of(vals):>10.2f}"
          f"{max(vals)-min(vals):>12.2f}{stdev_of(vals):>12.2f}")
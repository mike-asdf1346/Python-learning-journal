# special icon: █ ⁛⁘⸭ ⚌
from time import sleep as t
n = 100 
icon = "⁛⁛⁘⁘⸭⸭"
for i in range(1, n + 1):
    print(f"\r{icon[i % 6]} [{"█" * (i - 1)}{" " * (n - i)}] {round(i * 100 / n, 1)}%", end=" ", flush=True)
    t(0.1)
print("\nDownload Succeed!")
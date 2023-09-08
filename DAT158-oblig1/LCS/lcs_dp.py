import time

# Klasse for rekursiv LCS-beregning
class LCS_rec:
    def calculate(self, str1, str2, i, j):
        if i == 0 or j == 0:
            return 0
        if str1[i-1] == str2[j-1]:
            return 1 + self.calculate(str1, str2, i-1, j-1)
        else:
            return max(self.calculate(str1, str2, i-1, j), self.calculate(str1, str2, i, j-1))

# Klasse for dynamisk LCS-beregning
class LCS_dp:
    def calculate(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

# Opprett instanser av klassene
lcs_recursive_instance = LCS_rec()
lcs_dynamic_instance = LCS_dp()

# Test med forskjellige strenglengder og mål tiden
for n in range(1, 30):
    str1 = "a" * n
    str2 = "b" * n
    
    # Mål tiden for den rekursive versjonen
    start = time.time()
    lcs_recursive_instance.calculate(str1, str2, len(str1), len(str2))
    end = time.time()
    print(f"Rekursiv n={n}: {end - start} sekunder")

    # Mål tiden for den dynamiske versjonen
    start = time.time()
    lcs_dynamic_instance.calculate(str1, str2)
    end = time.time()
    print(f"Dynamisk n={n}: {end - start} sekunder")
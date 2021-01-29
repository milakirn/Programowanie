def przeliczanie(prawdz_gb):
    bajt = prawdz_gb * 1000000000
    return round(bajt / 1024 / 1024 / 1024, 2)

if __name__ == "__main__":
    GB = float(input("Podaj swoją pojemność dysku twardego w Gigabajtach: "))
    print(f"Prawdziwa pojemność dysku wynosi {przeliczanie(GB)} Gigabajtów.")
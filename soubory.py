from zadani_uzivatele import zadej_informaci

def vytvor_soubor(jmeno_souboru, hlavicka):
    with open(jmeno_souboru, mode="w") as file:
        jmeno, prijmeni, vek = hlavicka
        text = f"{jmeno},{prijmeni},{vek}" + "\n"
        file.writelines(text)


def zapis_do_souboru(jmeno_souboru, zapisuji):
    with open(jmeno_souboru, mode="a") as file:
        jmeno, prijmeni, vek = zapisuji
        text = f"{jmeno},{prijmeni},{vek}" + "\n"
        file.writelines(text)


def nahraj_csv_soubor(jmeno_souboru):
    with open(jmeno_souboru, mode="r") as file:
        data = file.readlines()
    return data

def pracuji_se_soubory():
    mode = input("Co chces delat? Zapisovat -> (z) nebo prace s daty (p):").lower()

    if mode == "z":
        vytvorit = input("Chces vytvorit soubor -> (y) nebo soubor jiz existuje (e):").lower()
        if vytvorit == "y":
            jmeno_souboru = input("Zadej jmeno souboru vcetne .csv")
            vytvor_soubor(jmeno_souboru, hlavicka=["Jmeno", "Prijmeni", "Vek"])
            print(f"Vytvořil jsem soubor {jmeno_souboru}")

        elif vytvorit == "e":
            jmeno_souboru = input("Zadej jmeno existujiciho souboru vcetne .csv")
            list_pro_zapis = zadej_informaci()
            zapis_do_souboru(jmeno_souboru, list_pro_zapis)
            print(f"Zapsal jsem: {list_pro_zapis}")
        else:
            print("Neco se nepovedlo")

    elif mode == "p":
        jmeno_souboru = input("Zadej jmeno existujiciho souboru vcetne .csv")
        data = nahraj_csv_soubor(jmeno_souboru)
        for radek in data:
            print(radek)
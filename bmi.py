# Yksinkertainen painoindeksin laskuri


# Kysytaan pituutta ja painoa
syote = input("Anna pituus (senteissä): ")
pituus= int(syote)
syote = input("Anna paino (kilogrammoissa): ")
paino = int(syote)


# Lasketaan painoindeksi
painoindeksi = round(float(paino / ((pituus / 100) ** 2)), 1)


# Verrataan painoindeksia
if (painoindeksi < 15):
    print("Painoindeksi on", painoindeksi, "(Sairaalloinen alipaino)")
elif (15 <= painoindeksi < 17):
    print("Painoindeksi on", painoindeksi, "(Merkittävä alipaino)")
elif (17 <= painoindeksi < 18.5):
    print("Painoindeksi on", painoindeksi, "(Normaalia alhaisempi paino)")
elif (18.5 <= painoindeksi < 25):
    print("Painoindeksi on", painoindeksi, "(Normaali paino)")
elif (25 <= painoindeksi < 30):
    print("Painoindeksi on", painoindeksi, "(Lievä ylipaino)")
elif (30 <= painoindeksi < 35):
    print("Painoindeksi on", painoindeksi, "(Merkittävä ylipaino)")
elif (35 <= painoindeksi < 40):
    print("Painoindeksi on", painoindeksi, "(Vaikea ylipaino)")
elif (painoindeksi >= 40):
    print("Painoindeksi on", painoindeksi, "(Sairaalloinen ylipaino)")


# Kysytaan tavoiteindeksia
syote = input("Anna tavoiteindeksi: ")
tavoite_indeksi = float(syote)
tiputettava = round(float((paino - (tavoite_indeksi / painoindeksi) * paino)), 1)


if (tiputettava < 0):
    print("Painoa tulisi kerätä", -tiputettava, "kilogrammaa.")
else:
    print("Painoa tulisi tiputtaa", tiputettava, "kilogrammaa.")


print("Kiitos ohjelman käytöstä.")

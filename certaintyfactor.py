penyakit = {
    "P01": {"nama": "A", "Gejala": ["G01", "G03"]},
    "P02": {"nama": "B", "Gejala": ["G02", "G03", "G04"]},
    "P03": {"nama": "C", "Gejala": ["G02", "G04"]},
    "P04": {"nama": "D", "Gejala": ["G01", "G04", "G05", "G06"]}
}

gejala = {
    "G01": {"nama": "Pusing", "nPakar": 0.8},
    "G02": {"nama": "Keringan Dingin", "nPakar": 0.6},
    "G03": {"nama": "Menggigil", "nPakar": 0.5},
    "G04": {"nama": "Dehidrasi", "nPakar": 0.2},
    "G05": {"nama": "Batuk", "nPakar": 0.5},
    "G06": {"nama": "Nyeri Tenggorokan", "nPakar": 0.5}
}

penyakit_pasien1 = {
    "G01": 0.5,
    "G02": 0.3,
    "G03": 0.2,
    "G04": 0.4,
    "G05": 0.8
}
# Cf[H,E]1 = Cf[H]1 x Cf[E]1


for i in penyakit_pasien1:
    print(gejala[i]["nPakar"], "x", penyakit_pasien1[i], " = ",
          gejala[i]["nPakar"] * penyakit_pasien1[i])


proses_lanjut = {
    kode_penyakit: {"jumlah_keluar": 0, "nilai": []} for kode_penyakit in penyakit
}


for kode_gejala in penyakit_pasien1:
    for kode_penyakit, data_penyakit in penyakit.items():
        if kode_gejala in data_penyakit["Gejala"]:
            proses_lanjut[kode_penyakit]["jumlah_keluar"] += 1
            proses_lanjut[kode_penyakit]["nilai"].append(
                gejala[kode_gejala]["nPakar"] * penyakit_pasien1[kode_gejala]
            )

print(proses_lanjut)

hasil_akhir = {kode_penyakit: 0 for kode_penyakit in penyakit}

for kode_penyakit, data_penyakit in proses_lanjut.items():
    nilai = data_penyakit["nilai"]
    cf = 0

    for value in nilai:
        cf = cf + value * (1 - cf)
    hasil_akhir[kode_penyakit] = cf


print(hasil_akhir)

print("Pasien menderita Penyakit : ", penyakit[max(hasil_akhir)]["nama"])

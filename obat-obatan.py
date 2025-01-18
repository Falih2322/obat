# Daftar obat dan harga
obat_list = [
    {
        "obat": "Paracetamol",
        "kegunaan": "Obat penurun demam, pereda nyeri ringan hingga sedang, dan antiinflamasi.",
        "harga": "Rp 2.000 - Rp 5.000",
    },
    {
        "obat": "Ibuprofen",
        "kegunaan": "Obat antiinflamasi non-steroid (NSAID) untuk meredakan peradangan, nyeri, dan demam.",
        "harga": "Rp 5.000 - Rp 15.000",
    },
    {
        "obat": "Amoxicillin",
        "kegunaan": "Antibiotik untuk mengobati berbagai infeksi bakteri seperti infeksi saluran pernapasan dan infeksi telinga.",
        "harga": "Rp 10.000 - Rp 30.000",
    },
    {
        "obat": "Amlodipine",
        "kegunaan": "Obat antihipertensi untuk mengontrol tekanan darah tinggi dan membantu mengobati angina (nyeri dada).",
        "harga": "Rp 10.000 - Rp 25.000",
    },
    {
        "obat": "Cetirizine",
        "kegunaan": "Antihistamin untuk mengobati alergi seperti rinitis alergi, mata gatal, dan gatal-gatal.",
        "harga": "Rp 5.000 - Rp 15.000",
    },
    {
        "obat": "Omeprazole",
        "kegunaan": "Obat untuk mengatasi gangguan pencernaan seperti maag, GERD (gastroesophageal reflux disease), dan tukak lambung.",
        "harga": "Rp 10.000 - Rp 30.000",
    },
    {
        "obat": "Dexamethasone",
        "kegunaan": "Obat kortikosteroid untuk mengurangi peradangan dan digunakan pada kondisi autoimun, alergi berat, dan infeksi.",
        "harga": "Rp 5.000 - Rp 15.000",
    },
    {
        "obat": "Chlorpheniramine",
        "kegunaan": "Obat antihistamin yang digunakan untuk mengatasi gejala alergi seperti bersin, hidung tersumbat, dan gatal-gatal.",
        "harga": "Rp 3.000 - Rp 10.000",
    },
    {
        "obat": "Metformin",
        "kegunaan": "Obat untuk mengatur kadar gula darah pada pasien diabetes tipe 2.",
        "harga": "Rp 10.000 - Rp 40.000",
    },
    {
        "obat": "Loperamide",
        "kegunaan": "Obat untuk mengobati diare dengan mengurangi pergerakan usus.",
        "harga": "Rp 5.000 - Rp 15.000",
    },
]

# Menampilkan daftar obat beserta kegunaan dan harga
print("Daftar Obat yang Sering Digunakan di Indonesia:")
print("=" * 50)
for index, obat in enumerate(obat_list, 1):
    print(f"{index}. {obat['obat']}")
    print(f"   Kegunaan: {obat['kegunaan']}")
    print(f"   Perkiraan Harga: {obat['harga']}")
    print("=" * 50)

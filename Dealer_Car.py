# List tipe domestik yang tersedia
domestic_types = ["ADM", "EDM", "JDM",]

# List brand mobil yang tersedia
brands = ["Toyota", "Honda", "Nissan", "Mitsubishi", "Subaru", "Porsche", "Lamborghini", "Ferrari", "BMW", "Mercedes-Benz", "Tesla", "Ford", "Chevrolet", "SRT", "Jeep", "Audi", "koeniggsegg", "Pagani", "Bugatti"]

# Dictionary model mobil yang tersedia untuk tiap brand
models = {
    "Toyota": {
        "GR86": {
            "year": 2021,
            "engine": "2.4L Flat-4 NA",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 230,
            "torque": 250,
            "weight": 1270,
            "price": 1000500000,
        },
        "GR Supra": {
            "year": 2021,
            "engine": "3.0L 6 Inline Twin-Turbocharged",
            "gearbox": "8-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 380,
            "torque": 500,
            "weight": 1540,
            "price": 2000000000,
        },
        "GR Yaris": {
            "year": 2021,
            "engine": "1.6L 3 Inline",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 260,
            "torque": 360,
            "weight": 1280,
            "price": 400000000,
        },
        "GT86": {
            "year": 2015,
            "engine": "2.4L Flat-4",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 200,
            "torque": 205,
            "weight": 1240,
            "price": 875000000,
        },
        "AE86": {
            "year": 1986,
            "engine": "1.6L 4 Inline",
            "gearbox": "5-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 130,
            "torque": 150,
            "weight": 950,
            "price": 500000000,
        },
        "Supra Turbo": {
            "year": 1999,
            "engine": "3.0L 6 Inline Twin-Turbocharged",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 320,
            "torque": 315,
            "weight": 1735,
            "price": 1500000000,
        },
    },
    "Honda": {
        "NSX": {
            "year": 2021,
            "engine": "3.5L V6 Twin-Turbocharged with Electric Motors",
            "gearbox": "9-Speed Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 570,
            "torque": 650,
            "weight": 1725,
            "price": 2500000000,
        },
        "Civic Type-R": {
            "year": 2021,
            "engine": "2.0L 4-silinder",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "FWD",
            "power": 300,
            "torque": 400,
            "weight": 1420,
            "price": 800000000,
        },
    },
    "Nissan": {
        "350Z": {
            "year": 2008,
            "engine": "3.5L V6",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 310,
            "torque": 360,
            "weight": 1530,
            "price": 300000000,
        },
        "370Z": {
            "year": 2023,
            "engine": "3.7L V6",
            "gearbox": "7-Speed Automatic Gearbox",
            "drivetrain": "RWD",
            "power": 332,
            "torque": 270,
            "weight": 1498,
            "price": 1200000000,
        },
        "180SX": {
            "year": 1996,
            "engine": "2.0L 4 Inline Turbocharged",
            "gearbox": "5-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 205,
            "torque": 275,
            "weight": 1180,
            "price": 700000000,
        },
        "240SX": {
            "year": 1998,
            "engine": "2.4L 4 Inline",
            "gearbox": "5-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 155,
            "torque": 180,
            "weight": 1250,
            "price": 500000000,
        },
        "Silvia S14": {
            "year": 1995,
            "engine": "2.0L 4-silinder",
            "gearbox": "5-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 220,
            "torque": 210,
            "weight": 1230,
            "price": 600000000,
        },
        "Silvia S15": {
            "year": 2001,
            "engine": "2.0L 4-silinder",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 240,
            "torque": 270,
            "weight": 1250,
            "price": 400000000,
        },
        "Skyline GT-R R32": {
            "year": 1994,
            "engine": "2.6L Twin-Turbocharged Inline-6",
            "gearbox": "5-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 300,
            "torque": 350,
            "weight": 1430,
            "price": 1000000000,
        },
        "Skyline GT-R R33": {
            "year": 1998,
            "engine": "2.6L Twin-Turbocharged Inline-6",
            "gearbox": "5-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 320,
            "torque": 370,
            "weight": 1540,
            "price": 1500000000,
        },
        "Skyline GT-R R34": {
            "year": 2002,
            "engine": "2.6L Twin-Turbocharged Inline-6",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 340,
            "torque": 400,
            "weight": 1560,
            "price": 2800000000,
        },
        "GT-R R35": {
            "year": 2016,
            "engine": "3.8L V6 Twin-Turbocharged",
            "gearbox": "7-Speed Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 600,
            "torque": 650,
            "weight": 1800,
            "price": 4000000000,
        },
    },
    "Mitsubishi": {
        "Eclipse": {
            "year": 2006,
            "engine": "2.4L 4-silinder",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "FWD",
            "power": 265,
            "torque": 260,
            "weight": 1400,
            "price": 400000000,
        },
        "EVO IX MR": {
            "year": 2006,
            "engine": "2.0L 4-silinder",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 280,
            "torque": 400,
            "weight": 1460,
            "price": 680000000,
        },
        "EVO X": {
            "year": 2010,
            "engine": "2.0L 4-silinder",
            "gearbox": "6-Speed Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 350,
            "torque": 550,
            "weight": 1600,
            "price": 700000000,
        },
        "3000GT": {
            "year": 1999,
            "engine": "3.0L V6 Twin-Turbocharged",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 320,
            "torque": 315,
            "weight": 1735,
            "price": 1500000000,
        },
    },
    "Subaru": {
        "BRZ": {
            "year": 2023,
            "engine": "2.4L Flat-4",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 228,
            "torque": 184,
            "weight": 2789,
            "price": 850000000,
        },      
        "Imprezza WRX STI": {
            "year": 2023,
            "engine": "2.5L Flat-4 Turbocharged",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 310,
            "torque": 394,
            "weight": 1575,
            "price": 850000000,
        },
    },
    "Audi": {
        "R8": {
            "year": 2023,
            "engine": "5.2L V10 NA",
            "gearbox": "7-Speed Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 562,
            "torque": 406,
            "weight": 1715,
            "price": 8000000000,
        },       
        "RS5": {
            "year": 2023,
            "engine": "2.9L 6 Inline Turbocharged",
            "gearbox": "8-Speed Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 450,
            "torque": 600,
            "weight": 1575,
            "price": 2600000000,
        },
        "TT": {
            "year": 2023,
            "engine": "2.0L 4-Inline",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "AWD",
            "power": 335,
            "torque": 450,
            "weight": 1335,
            "price": 142000000,
        },
    },
    "Bugatti": {
        "Veyron": {
            "year": 2023,
            "engine": "8.0L Quad-Turbocharged W16",
            "gearbox": "7-Speed Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 1200,
            "torque": 1500,
            "weight": 1888,
            "price": 2000000,
        },
        "Chiron": {
            "year": 2023,
            "engine": "8.0L Quad-Turbocharged W16",
            "gearbox": "7-Speed Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 1500,
            "torque": 1600,
            "weight": 1995,
            "price": 3000000,
        },
    },
    "Koeniggsegg": {
        "Jesko": {
            "year": 2023,
            "engine": "5.0L V8 Twin-Turbocharged",
            "gearbox": "9-Speed Multi-Clutch Transmission",
            "drivetrain": "RWD",
            "power": 1280,
            "torque": 1500,
            "weight": 1320,
            "price": 3000000,
        },
        "Gemera": {
            "year": 2023,
            "engine": "2.0L 3-cylinder Twin-Turbocharged with Electric Motors",
            "gearbox": "Direct Drive",
            "drivetrain": "AWD",
            "power": 1700,
            "torque": 3500,
            "weight": 1850,
            "price": 1700000,
        },
        "Agera-R": {
            "year": 2023,
            "engine": "5.0L V8 Twin-Turbocharged",
            "gearbox": "7-Speed Multi-Clutch Transmission",
            "drivetrain": "RWD",
            "power": 1140,
            "torque": 1200,
            "weight": 1330,
            "price": 2500000
        },
        "CCX": {
            "year": 2023,
            "engine": "4.7L V8 Twin-Supercharged",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 806,
            "torque": 920,
            "weight": 1280,
            "price": 2000000
        },
    },
    "Pagani": {
        "Huayra": {
            "year": 2023,
            "engine": "6.0L Twin-Turbocharged V12",
            "gearbox": "7-Speed Automated Manual Gearbox",
            "drivetrain": "RWD",
            "power": 791,
            "torque": 775,
            "weight": 1350,
            "price": 3000000,
        },
    },
    "Porsche": {
        "911 Turbo S": {
            "year": 2023,
            "engine": "3.8L Twin-Turbocharged Flat-6",
            "gearbox": "8-Speed PDK Dual-Clutch Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 640,
            "torque": 590,
            "weight": 1640,
            "price": 4000000,
        },
        "Cayman GTS": {
            "year": 2023,
            "engine": "4.0L Flat-6",
            "gearbox": "6-Speed Manual Gearbox",
            "drivetrain": "RWD",
            "power": 394,
            "torque": 309,
            "weight": 3131,
            "price": 1200000,
        },
        "Taycan Turbo S": {
            "year": 2023,
            "engine": "Electric Motors",
            "gearbox": "2-Speed Automatic Gearbox",
            "drivetrain": "AWD",
            "power": 750,
            "torque": 774,
            "weight": 5160,
            "price": 2500000,
        },
    },
}

import os
import random

# Nama dealer
dealer_name = "Fanny Motorsport"

# Menampilkan tipe domestik yang tersedia
print("Selamat datang di", dealer_name)
print("Berikut tipe domestik yang tersedia:")
for dom_type in domestic_types:
    print("- " + dom_type)
domestic_selected = input("Silahkan ketik Tipe Domestik yang anda mau cari di toko kami: ")

# Memilih brand mobil berdasarkan tipe domestik
if domestic_selected == "JDM":
    brands = ["Toyota", "Honda", "Nissan", "Mitsubishi", "Subaru"]
elif domestic_selected == "EDM":
    # Tambahkan brand Eropa jika dibutuhkan
    brands = ["Mercedes-Benz", "BMW", "Audi", "Ferrari", "Lamborghini", "Porsche", "Koeniggsegg", "Bugatti", "Pagani"]
elif domestic_selected == "ADM":
    # Tambahkan brand Amerika jika dibutuhkan
    brands = ["Ford", "Chevrolet", "Tesla", "SRT", "Jeep"]
else:
    print("Tipe domestik tidak valid.")
    exit()

# memilih brand mobil
print("Berikut brand mobil yang tersedia di dealer kami:")
for brand in brands:
    print("- " + brand)
brand_selected = input("Silahkan ketik brand apa yang anda mau cari di toko kami: ")

# memilih model mobil
model_selected = None

while True:
    if brand_selected in models:
        print("Model mobil yang tersedia untuk brand " + brand_selected + ":")
        for model in models[brand_selected]:
            print("- " + model)
        model_selected = input("Silahkan ketik model apa yang anda mau cari: ")
        if model_selected in models[brand_selected]:
            print("\nKami menyediakan mobil sesuai dengan yang anda minta. Berikut detail mobil yang dipilih:")
            print("Brand:", brand_selected)
            print("Model:", model_selected)
            print("Tahun Pembuatan:", str(models[brand_selected][model_selected]["year"]))
            print("Mesin:", models[brand_selected][model_selected]["engine"])
            print("Gearbox:", models[brand_selected][model_selected]["gearbox"])
            print("Sistem Penggerak:", models[brand_selected][model_selected]["drivetrain"],)
            power = models[brand_selected][model_selected]["power"]
            formatted_power = "{:,.0f}".format(power)
            print("Tenaga:", formatted_power, "HP")
            torque = models[brand_selected][model_selected]["torque"]
            formatted_torque = "{:,.0f}".format(torque)
            print("Torsi:", formatted_torque, "Nm")
            weight = models[brand_selected][model_selected]["weight"]
            formatted_weight = "{:,.0f}".format(weight)
            print("Berat:", formatted_weight, "Kg")
            print("Warna:", random.choice(["Putih", "Merah", "Hijau", "Hitam", "Silver", "Kuning"]))
            price = models[brand_selected][model_selected]["price"]
            formatted_price = "{:,.2f}".format(price)
            output = "Harga: Rp. {}-".format(formatted_price.replace(",", "."))
            print(output)

            # Meminta konfirmasi untuk membeli mobil
            confirm = input("Apakah anda ingin membeli mobil ini? (y/n) ")
            if confirm == "y":
                # Menghapus mobil yang dibeli dari dictionary
                del models[brand_selected][model_selected]
                print(
                    "Terima kasih telah membeli mobil dari kami. Silahkan selesaikan registrasi anda dan kami akan mengantarkan mobil anda ke rumah anda!"
                )
            else:
                print("Terima kasih telah berkunjung ke", dealer_name + ".")
            # Jika tidak ada model mobil lagi untuk brand yang dipilih
            if not models[brand_selected]:
                # Menghapus brand dari dictionary jika tidak ada model mobil lagi
                del models[brand_selected]
            break
        else:
            print("Maaf, kami tidak menyediakan mobil yang anda inginkan.")
    else:
        print("Maaf, kami tidak menyediakan brand yang anda cari.")

    search_again = input("Apakah Anda ingin mencari brand lain? (y/n) ")
    if search_again == "y":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        brand_selected = input(
            "Silahkan ketik brand apa yang anda mau cari di toko kami: "
        )
    else:
        print("Terima kasih telah berkunjung ke", dealer_name + ".")
        break

def check_car_availability(brand, model):
    if brand in models and model in models[brand]:
        return True
    else:
        return False

# Fungsi untuk memeriksa keberadaan mobil setelah transaksi
if not check_car_availability(brand_selected, model_selected):
    print("\nMobil", brand_selected, model_selected, "telah berhasil dijual.")
else:
    print("\nMobil", brand_selected, model_selected, "masih tersedia.")
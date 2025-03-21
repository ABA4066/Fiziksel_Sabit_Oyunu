import random
import time

puan = 0
class Sabitler():
    tum_sabitler = []
    def __init__(self, sira, deger, sembol, isim):
        self.sira = sira
        self.deger = deger
        self.sembol = sembol
        self.isim = isim
        Sabitler.tum_sabitler.append(self)

Sabitler(1, "6.67 × 10⁻¹¹ m³/kg·s²", "G", "Evrensel Kütle Çekim Sabiti")
Sabitler(2, "299.792.458 m/s", "c", "Işık Hızı")
Sabitler(3, "6,62 × 10⁻³⁴ J·s", "h", "Planck Sabiti")
Sabitler(4, "1,602 × 10⁻¹⁹ C", "e", "Temel Yük")
Sabitler(5, "6,02 × 10²³ mol⁻¹", "Na", "Avogadro Sayısı")
Sabitler(6, "0,082 litre·atm/mol·K", "R", "İdeal Gaz Sabiti")
Sabitler(7, "4π × 10⁻⁷ N/A²", "mu0", "Manyetik Geçirgenlik Sabiti")
Sabitler(8, "8,85 × 10⁻¹² F/m", "e0", "Elektriksel Geçirgenlik Sabiti")
Sabitler(9, "9,10 × 10⁻³¹ kg", "me", "Elektron Kütlesi")
Sabitler(10, "1,672 × 10⁻²⁷ kg", "mp", "Proton Kütlesi")
Sabitler(11, "5,67 × 10⁻⁸ W/(m²·K⁴)", "sigma", "Stefan-Boltzmann Sabiti")
Sabitler(12, "1,0973731568508 × 10⁷ m⁻¹", "R", "Rydberg Sabiti")
Sabitler(13, "(67 – 74) km/s/Mpc", "H0", "Hubble Sabiti")
Sabitler(14, "1,4 M☉", "ℏ", "Chandrasekhar Limiti")
Sabitler(15, "1,98 × 10³⁰ kg", "M0", "Güneş Kütlesi")
Sabitler(16, "6,95 × 10⁸ m", "R0", "Güneş Yarıçapı")
Sabitler(17, "9,81 m/s²", "g", "Yerçekimi İvmesi")
Sabitler(18, "1,3 × 10³¹ W", "ℏ", "Eddington Limiti")
Sabitler(19, "1,496 × 10⁸ km", "AB", "Astronomik Birim")
Sabitler(20, "3,26 ışık yılı", "pc", "Parsek")
Sabitler(21, "5772 K", "T0", "Güneş Sıcaklığı")

print("""*******************

Temel Fiziksel Sabitleri Tahmin Oyunu

Hoş geldiniz !!

Başlamak için '1' e basın

Çıkmak için 'q' ya basın.
*******************\n""")

while True:
    print(f"Şu anki puanınız: {puan}")
    secim = input("Devam etmek için '1', çıkmak için 'q' ya basın:\n")

    if secim == "q":
        print(f"Oyundan çıkılıyor... Son puanınız: {puan}\n")
        time.sleep(2)
        break
    elif secim == "1":
        rastgele_sabit = random.choice(Sabitler.tum_sabitler)
        print(f"Bu hangi sabit? Değer: {rastgele_sabit.deger}\n")

        tahmin = input("Sembol veya ismini girin:\n").strip()

        if tahmin.lower() == rastgele_sabit.sembol.lower() or tahmin.lower() == rastgele_sabit.isim.lower():
            print("Doğru! +10 puan kazandınız.\n")
            puan += 10
        else:
            print(f"Yanlış! Doğru cevap: {rastgele_sabit.isim} ({rastgele_sabit.sembol})\n")
            puan = max(0, puan - 5)

        time.sleep(2)

    else:
        print("Yanlış giriş! Lütfen '1' veya 'q' girin.\n")
        time.sleep(2)
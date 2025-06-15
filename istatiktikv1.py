# İlk iş olarak gerekli kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
from scipy import stats

# CSV dosyasını okuyoruz
veri = pd.read_csv(r"C:\Users\kacan\Downloads\tsl_dataset.csv")

# İlk 5 satırı kontrol ediyoruz
print(veri.head())

#ben toplam gol sayısı verisinden ilerleyeceğim verinin adı da totgoal olarak tanımlanmış

# Toplam gol sütunu üzerinden istatistikleri hesaplıyoruz

ortalama = np.mean(veri["totgoal"])  # Ortalama
medyan = np.median(veri["totgoal"])  # Medyan
varyans = np.var(veri["totgoal"], ddof=1)  # Varyans
sapma = np.std(veri["totgoal"], ddof=1)  # Standart sapma
hata = stats.sem(veri["totgoal"])  # Standart hata

# Sonuçları yazdırıyoruz
print("Ortalama:", round(ortalama, 3))
print("Medyan:", medyan)
print("Varyans:", round(varyans, 3))
print("Standart Sapma:", round(sapma, 3))
print("Standart Hata:", round(hata, 3))

#unuttuğum için matplotlibi şimdi ekliyorum
import matplotlib.pyplot as plt

# Histogram çizimi (renkleri fenerbahçeli olduğum için sarı ve mavi seçtim
plt.hist(veri["totgoal"], bins=15, color="yellow", edgecolor="blue")
plt.title("Toplam Gol Dağılımı (Histogram)")
plt.xlabel("Maç Başına Toplam Gol")
plt.ylabel("Maç Sayısı")
plt.grid(True)
plt.show()

# Boxplot çizimi
plt.boxplot(veri["totgoal"], vert=False)
plt.title("Toplam Gol (Boxplot)")
plt.xlabel("Gol Sayısı")
plt.grid(True)
plt.show()

# Güven aralığını hesaplayalım 

n = len(veri["totgoal"])     # Toplam maç sayısı
guven = 0.95                 # Güven düzeyi

# t-tablosundan kritik değer alınır
t_kritik = stats.t.ppf((1 + guven) / 2, df=n - 1)

# Alt ve üst sınır hesaplanır
alt_sinir = ortalama - t_kritik * hata
ust_sinir = ortalama + t_kritik * hata

# Sonuç yazdırılır
print("95% güven aralığı: ", round(alt_sinir, 3), "ile", round(ust_sinir, 3))

#Hipotez testi yapıyoruz  Ortalama 2.5 mi? 

istenen_ortalama = 2.5  # test etmek istediğimiz değer

# t testi ile farkı ölçüyoruz
t_deger, p_deger = stats.ttest_1samp(veri["totgoal"], istenen_ortalama)

# Sonuçları yazdırıyoruz
print("t değeri:", round(t_deger, 3))
print("p değeri:", round(p_deger, 4))

# Karar veriyoruz
if p_deger < 0.05:
    print("H₀ reddedildi → Ortalama 2.5 değildir.")
else:
    print("H₀ reddedilemez → Ortalama 2.5 olabilir.")

# Örneklem büyüklüğü hesaplanıyor

Z_degeri = 1.645       # %90 güven düzeyi için Z değeri
E = 0.1                # Maksimum kabul edilen hata payı
gerekli_orneklem = (Z_degeri * sapma / E) ** 2

print("Gerekli minimum örneklem sayısı:", round(gerekli_orneklem))


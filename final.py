import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#  VERİLERİ OKUMA
calisma_data = pd.read_csv("ogrenci_calisma_aliskanliklari.csv")
not_data = pd.read_csv("ogrenci_akademik_basari.csv")

# ÇALIŞMA VERİSİNİ DÜZENLEME

calisma_duzenli = calisma_data[["Ogrenci_ID", "Haftalik_Calisma_Suresi"]].copy()

# BAŞARI VERİSİNİ DÜZENLEME

not_duzenli = not_data[["Ogrenci_ID", "Final_Notu"]].copy()

# TABLOLARI BİRLEŞTİRME

tablo = pd.merge(calisma_duzenli, not_duzenli, on=["Ogrenci_ID"], how="inner")

# Eksik veri olan satırları temizliyoruz.
tablo = tablo.dropna()

# GRAFİK ÇİZME

cerceve, eksen = plt.subplots(figsize=(10, 6))

# GRAFİK AYARLARI

eksen.set_xlabel('Haftalık Çalışma Süresi')
eksen.set_ylabel('Dönem Sonu Notu (0-20)', color='#1f77b4')

# SCATTER PLOT (Dağılım)

jitter_x = tablo["Haftalik_Calisma_Suresi"] + np.random.normal(0, 0.08, size=len(tablo))

# Çizim 
cizim1 = eksen.scatter(jitter_x, tablo["Final_Notu"], 
                       alpha=0.5, color='#1f77b4', s=50, label="Öğrenci Notları")

# TREND ÇİZGİSİ (Ortalama)

grup_ortalamalari = tablo.groupby("Haftalik_Calisma_Suresi")["Final_Notu"].mean()
cizim2 = eksen.plot(grup_ortalamalari.index, grup_ortalamalari.values, 
                    color='red', linewidth=2.5, marker='o', label="Ortalama Başarı")

# EKSEN DÜZENLEMELERİ

eksen.set_xticks([1, 2, 3, 4])
eksen.set_xticklabels(['< 2 Saat', '2 - 5 Saat', '5 - 10 Saat', '> 10 Saat'])
eksen.grid(True, linestyle='--', alpha=0.5)

# LEJANT (Açıklama Kutusu)

eksen.legend(loc="upper left")

plt.title("Öğrencilerin Çalışma Süresi ve Başarı İlişkisi")
plt.show()
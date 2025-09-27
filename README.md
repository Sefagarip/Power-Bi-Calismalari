# Power BI Analiz Projeleri

Bu repository, Power BI ve Python kullanılarak gerçekleştirilen veri analizi projelerini içermektedir.

## 📁 Proje Yapısı

### FUTBOL Klasörü
Futbol verileri analizi için geliştirilen araçlar ve raporlar:

- **`futbol.pbix`**: Futbol istatistikleri Power BI raporu
- **`Haftalık İstatislikler.py`**: Haftalık maç verilerini çeken Python script
- **`Sezon İstatislikleri.py`**: Sezon bazında takım ve oyuncu istatistiklerini toplayan script
- **`saha.png`**: Futbol sahası görsel elementi

#### Futbol Scripti Özellikleri:
- Futbol API entegrasyonu
- MSSQL veritabanı bağlantısı
- Haftalık maç verileri (maç sonuçları, oranlar, istatistikler)
- Oyuncu ve takım istatistikleri
- Momentum analizi
- Şut ve koordinat verileri

### SOSYAEKONEMİ Klasörü
Sosyoekonomik veri analizi projeleri:

- **`Sosyoekonomik seviyesi ile sisyasi partilerin karşılaştırlıması.pbix`**: Sosyoekonomik durum ve siyasi tercihler arasındaki ilişkiyi analiz eden Power BI raporu
- **`iller.json`**: İl bazında sosyoekonomik veriler
- **`ilçeler.json`**: İlçe bazında sosyoekonomik veriler
- **`ilçe2.json`**: Güncellenmiş ilçe verileri

## 🛠️ Teknolojiler

- **Power BI**: Görselleştirme ve raporlama
- **Python**: Veri çekme ve işleme
  - pandas: Veri manipülasyonu
  - sqlalchemy: Veritabanı bağlantısı
  - datafc: Futbol verileri API'si
- **MSSQL**: Veri depolama

## 📊 Kullanım

### Futbol Analizleri
1. Python scriptlerini çalıştırarak verileri veritabanına aktarın
2. Power BI raporunu açarak güncel analizleri görüntüleyin

### Sosyoekonomik Analizler
1. JSON veri dosyalarını Power BI'a import edin
2. Sosyoekonomik-siyasi korelasyon analizlerini inceleyin

## 📋 Kurulum

```bash
# Gerekli Python kütüphanelerini yükleyin
pip install pandas sqlalchemy datafc pyodbc
```

## ⚠️ Notlar

- MSSQL bağlantı bilgilerinizi scriptlerde güncelleyiniz

## 📈 Analiz Kapsamı

- **Futbol**: Maç sonuçları, takım performansları, oyuncu istatistikleri
- **Sosyoekonomik**: Bölgesel gelişmişlik seviyeleri, siyasi tercih analizi


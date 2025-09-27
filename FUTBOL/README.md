# Futbol Analiz Projesi

Bu klasör, futbol verilerinin analizi için geliştirilen Power BI raporları ve Python scriptlerini içermektedir.

## 📁 Dosyalar

- **`futbol.pbix`**: Ana futbol istatistikleri Power BI raporu
- **`Haftalık İstatislikler.py`**: Haftalık maç verilerini çeken Python script
- **`Sezon İstatislikleri.py`**: Sezon bazında takım ve oyuncu istatistiklerini toplayan script
- **`saha.png`**: Futbol sahası görsel elementi

## 🔧 Script Özellikleri

### Haftalık İstatislikler
- Futbol API entegrasyonu
- MSSQL veritabanı bağlantısı
- Haftalık maç verileri (maç sonuçları, oranlar, istatistikler)
- Momentum analizi
- Şut ve koordinat verileri

### Sezon İstatislikleri
- Takım sıralamaları
- Oyuncu performans istatistikleri
- Takım bazında detaylı analiz
- Kadro bilgileri

## 📊 Power BI Rapor Görüntüleri

### Ana Dashboard
![Futbol Dashboard 1](Ekran%20görüntüsü%202025-09-27%20140807.jpg)

### Takım İstatistikleri
![Futbol Dashboard 2](Ekran%20görüntüsü%202025-09-27%20140836.jpg)

### Oyuncu Performansları
![Futbol Dashboard 3](Ekran%20görüntüsü%202025-09-27%20140925.jpg)

### Maç Analizleri
![Futbol Dashboard 4](Ekran%20görüntüsü%202025-09-27%20140953.jpg)

### Detaylı İstatistikler
![Futbol Dashboard 5](Ekran%20görüntüsü%202025-09-27%20141041.jpg)

## 🛠️ Kullanım

1. Python scriptlerini çalıştırarak verileri MSSQL veritabanına aktarın
2. Power BI raporunu açarak güncel analizleri görüntüleyin
3. Raporlarda interaktif filtreler kullanarak detaylı analizler yapın

## 📋 Gereksinimler

```bash
pip install pandas sqlalchemy datafc pyodbc
```

## ⚠️ Notlar

- MSSQL bağlantı bilgilerinizi scriptlerde güncelleyiniz
- Tournament ID ve Season ID parametrelerini ihtiyacınıza göre ayarlayın
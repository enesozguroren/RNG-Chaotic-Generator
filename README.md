# 🌀 Chaotic Random Number Generator (Logistic Map)

Bu proje, **Kaos Teorisi** prensiplerini kullanarak deterministik ancak tahmin edilemez rastgele sayılar üreten bir Python simülasyonudur. Matematiksel olarak "Lojistik Harita" (Logistic Map) denklemini temel alır.

## 🧐 Matematiksel Model
Kullanılan temel denklem:
$$x_{n+1} = r \cdot x_n \cdot (1 - x_n)$$

* **Tohum (Seed):** $x_0 = 0.23$
* **Kontrol Parametresi:** $r = 4.0$ (Tam Kaos Rejimi)

## 🚀 Başlarken

### Gereksinimler
Grafikleri görüntülemek için `matplotlib` kütüphanesine ihtiyacınız var:
```bash
pip install matplotlib

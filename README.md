

---

# Araba Sınıfı

Bu Python programı, Araba adında bir sınıf oluşturur. Her bir araba nesnesi, marka, model ve renk gibi özelliklere sahiptir.

## Nasıl Kullanılır

1. `araba_sinifi.py` dosyasını kullanmak istediğiniz Python projesinin dizinine kopyalayın.
2. Programınızda Araba sınıfını kullanmak için `araba_sinifi.py` dosyasını içe aktarın (import edin).
3. Araba sınıfından nesneler oluşturun ve özelliklerini belirtin.

## Örnek Kullanım

```python
from araba_sinifi import Araba

# Araba nesnelerini oluşturun
taksi = Araba("Mercedes", "E200", "Beyaz")
kamyon = Araba("Volvo", "FH16", "Kırmızı")
trakor = Araba("John Deere", "8R", "Yeşil")

# Araba özelliklerini ekrana yazdırın
print("Taksi Marka:", taksi.marka)
print("Kamyon Model:", kamyon.model)
print("Traktör Rengi:", trakor.renk)
```

## Geliştirme

Bu program basit bir Araba sınıfı oluşturur. Geliştirmek için şunları düşünebilirsiniz:

- Araba sınıfına yeni özellikler ekleyin (örneğin, yakıt tüketimi, hız vb.).
- Nesneler arasında işlem yapabilen yöntemler (metodlar) ekleyin (örneğin, hızlanma, fren yapma vb.).
- Sınıfı genişleterek diğer araç türlerini (kamyonet, otobüs, motosiklet vb.) temsil edecek şekilde ayarlayın.

## Lisans

Bu program MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---

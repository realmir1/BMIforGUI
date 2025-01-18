
# BMI (Vücut Kitle İndeksi) Hesaplama Uygulaması

Bu proje, kullanıcıların Vücut Kitle İndeksi'ni (BMI) hesaplamalarını sağlayan basit bir Python uygulamasıdır. Uygulama, kullanıcının boy ve kilo bilgilerini alarak BMI değerini hesaplar ve hangi kategoride olduğunu belirtir (Zayıf, Normal, Fazla Kilolu, Obez). Şık bir arayüz ve görsel ile kullanımı kolay bir tasarıma sahiptir.

---

## Özellikler

- **Kullanıcı dostu arayüz:** Kullanıcıdan boy ve kilo bilgilerini alarak kolay kullanım sağlar.  
- **BMI hesaplama:** BMI formülüne göre sonucu hesaplar ve detaylı kategori bilgisi sunar.  
- **Hata kontrolü:** Negatif veya geçersiz girişler için uyarı mesajları görüntülenir.  
- **Görsel destek:** Uygulama, arayüzün üst kısmında bir görsel içerir ve görsel estetiği artırır.  

---

## Gereksinimler

Bu uygulamayı çalıştırmadan önce aşağıdaki gereksinimlerin karşılandığından emin olun:

- **Python 3.x**: Uygulama Python 3 sürümleriyle uyumludur.
- **Tkinter**: GUI oluşturmak için kullanılır ve Python ile birlikte gelir.
- **Pillow (PIL)**: Görsel işleme için gereklidir.  
  Pillow kütüphanesini yüklemek için şu komutu kullanabilirsiniz:  
  ```bash
  pip install pillow
  ```

---

## Nasıl Kullanılır?

1. **Projeyi İndirin:**  
   Bu projeyi bilgisayarınıza klonlayın veya `.zip` dosyası olarak indirin.  

2. **Kod Düzenlemesi:**  
   - `image.open` kısmında belirtilen görsel dosya yolunu kendi görselinizin bulunduğu yere göre düzenleyin.  
   Örneğin:  
   ```python
   image = Image.open("/path/to/your/image.jpg")
   ```

3. **Uygulamayı Çalıştırın:**  
   Terminal veya IDE kullanarak aşağıdaki komutla uygulamayı çalıştırabilirsiniz:  
   ```bash
   python bmi_hesaplama.py
   ```

4. **Boy ve Kilo Bilgisi Girin:**  
   Uygulama açıldığında, boyunuzu (metre cinsinden) ve kilonuzu (kilogram cinsinden) girin. Ardından "Hesaplama" butonuna tıklayın.  

5. **Sonuçları Görüntüleyin:**  
   Hesaplama tamamlandığında, BMI değeriniz ve hangi kategoriye girdiğiniz ekranda görüntülenecektir.

---

## Projenin Çalışma Prensibi

### BMI Hesaplama Formülü:
```
BMI = Ağırlık (kg) / Boy (m)²
```

### BMI Kategorileri:
| BMI Aralığı       | Kategori              |
|--------------------|-----------------------|
| 18.5'ten düşük    | Zayıf                 |
| 18.5 - 24.9       | Normal               |
| 25 - 29.9         | Fazla Kilolu          |
| 30 ve üzeri       | Obez                 |

Uygulama, kullanıcıdan aldığı kilo ve boy bilgilerini kullanarak bu formüle göre BMI değerini hesaplar. Hesaplanan BMI değeri yukarıdaki kategorilere göre sınıflandırılır ve ekranda gösterilir.

---

## Örnek Ekran Görüntüsü

Uygulamanın şık ve kullanıcı dostu arayüzü aşağıdaki gibidir:

<p align="center"> <img src="https://github.com/realmir1/BMIforGUI/blob/main/Ekran%20Resmi%202025-01-19%2000.38.01.png?raw=true" , width="400", height="800"</p>

> **Not:** Yukarıdaki görsel, örnek bir kullanıcı arayüzü sunmak için eklenmiştir. Projeyi çalıştırmadan önce, kodda kullanılan görselin dosya yolunu doğru bir şekilde güncellemeyi unutmayın.

---

## Sorun Giderme

### 1. Görsel Yüklenmiyor:
Eğer uygulama çalıştığında görsel yüklenmiyorsa, `image.open` fonksiyonunda belirtilen dosya yolunun doğru olduğundan emin olun.  
Örneğin:  
```python
image = Image.open("/Users/kullanici/Desktop/image.jpg")
```

### 2. Pillow Kurulu Değil:
Hata mesajı alıyorsanız Pillow kütüphanesinin kurulu olduğundan emin olun:  
```bash
pip install pillow
```

---

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına göz atabilirsiniz.

---

**Geliştirici Notu:** Bu proje eğitim amaçlı oluşturulmuştur. BMI hesaplama sonuçları yalnızca bilgi amaçlıdır ve tıbbi tavsiye yerine geçmez. Sağlıkla ilgili endişeleriniz için bir sağlık uzmanına danışınız.
```

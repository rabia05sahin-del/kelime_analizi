CümleDedektif — Türkçe Kelime Öneri Sistemi

Proje Hakkında

CümleDedektif, Türkçe kelimeler arasındaki anlamsal benzerlikleri kullanarak girilen kelimeye benzer kelimeler öneren bir web uygulamasıdır. Proje, doğal dil işleme (NLP) yöntemlerinden yararlanır.

Kullanılan Teknolojiler

- Python
- Flask
- Gensim
- Word2Vec
- HTML

Nasıl Çalışır?

Kullanıcı web arayüzüne bir kelime girer. Uygulama, önceden eğitilmiş Türkçe kelime vektörleri modelini kullanarak girilen kelimeye anlamsal açıdan en yakın 10 kelimeyi bulur ve sonuçları ekranda gösterir.

Proje Dosyaları

- "app.py": Flask web uygulamasını ve kullanıcı isteklerini yönetir.
- "main.py": Kelime benzerliği işlemleri için kullanılan Python kodunu içerir.
- "templates/index.html": Kullanıcı arayüzünü oluşturur.
- "trModel100": Kelime vektörlerini içeren önceden eğitilmiş model dosyasıdır.

Kurulum

Gerekli kütüphaneleri yüklemek için:

pip install -r requirements.txt

Ardından uygulamayı çalıştırmak için:

python app.py

Not: Uygulamanın çalışması için "trModel100" model dosyasının doğru konumda bulunması gerekir.

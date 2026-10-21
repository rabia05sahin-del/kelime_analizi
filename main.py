
from gensim.models import KeyedVectors

print("Word2Vec modeli yükleniyor...")

model = KeyedVectors.load_word2vec_format(
    "trModel100",
    binary=True
)

print("Model başarıyla yüklendi!")


def kelime_oner():
    kelime = input("\nBenzer kelimelerini bulmak istediğin kelimeyi yaz: ")
    kelime = kelime.lower().strip()

    if kelime not in model:
        print("Bu kelime modelde bulunamadı.")
        return

    oneriler = model.most_similar(kelime, topn=10)

    print(f"\n'{kelime}' kelimesine benzer kelimeler:\n")

    for sira, (oneri, puan) in enumerate(oneriler, start=1):
        print(f"{sira}. {oneri} - Benzerlik: {puan:.2%}")


while True:
    kelime_oner()


from flask import Flask, render_template, request
from gensim.models import KeyedVectors

app = Flask(__name__)

print("Word2Vec modeli yükleniyor...")
model = KeyedVectors.load_word2vec_format(
    "trModel100",
    binary=True
)
print("Model hazır!")


@app.route("/", methods=["GET", "POST"])
def ana_sayfa():
    kelime = ""
    oneriler = []
    hata = ""

    if request.method == "POST":
        kelime = request.form.get("kelime", "").strip().lower()

        if not kelime:
            hata = "Lütfen bir kelime yaz."
        elif kelime not in model:
            hata = "Bu kelime modelde bulunamadı. Başka bir kelime dene."
        else:
            oneriler = model.most_similar(kelime, topn=10)

    return render_template(
        "index.html",
        kelime=kelime,
        oneriler=oneriler,
        hata=hata
    )


if __name__ == "__main__":
    app.run(debug=True)


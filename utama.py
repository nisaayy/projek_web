from flask import Flask, render_template, request

app = Flask(__name__)

# Data
daerah_cabang = {
    1: "Purwokerto",
    2: "Purbalingga",
    3: "Jakarta",
    4: "Bandung",
    5: "Yogyakarta"
}

jenis_room = {
    1: "Single Room",
    2: "Single Bed",
    3: "Suite Room",
    4: "Deluxe Room",
    5: "Presidential Suite"
}

harga = {
    1: [250000, 250000, 500000, 750000, 1000000],  # Purwokerto
    2: [200000, 200000, 450000, 700000, 950000],  # Purbalingga
    3: [500000, 500000, 750000, 900000, 1200000],  # Jakarta
    4: [400000, 400000, 550000, 750000, 900000],  # Bandung
    5: [250000, 250000, 400000, 600000, 750000]   # Yogyakarta
}

# Fungsi format untuk IDR
def format_idr(value):
    return f"IDR {value:,.0f}".replace(",", ".")

# Tambahkan filter ke Jinja
app.jinja_env.filters['format_idr'] = format_idr

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ambil data dari form
        nama = request.form.get("nama")
        pilih_cabang = int(request.form.get("hotel"))
        pilih_kamar = int(request.form.get("kamar"))
        lama_menginap = int(request.form.get("lama"))

        # Hitung total
        kamar_harga = harga[pilih_cabang][pilih_kamar - 1]
        total_harga = kamar_harga * lama_menginap

        # Hitung diskon
        diskon = 0
        if total_harga > 500000:
            diskon = total_harga * 0.12

        total_bayar = total_harga - diskon

        return render_template(
            "index.html",
            nama=nama,
            daerah=daerah_cabang[pilih_cabang],
            kamar=jenis_room[pilih_kamar],
            kamar_harga=kamar_harga,
            lama_menginap=lama_menginap,
            total_harga=total_harga,
            diskon=diskon,
            total_bayar=total_bayar
        )
    
    # Untuk GET, kirimkan variabel kosong
    return render_template("projek.html")

@app.route('/edit/', defaults={'filename': None})
@app.route('/edit/<filename>')
def edit(filename):
    if filename:
        return f"Editing {filename}"
    return "No filename provided."

if __name__ == "__main__":
    app.run(debug=True)

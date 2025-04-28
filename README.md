# 🚀𝐀𝐏𝐈 𝐏𝐫𝐞𝐝𝐢𝐤𝐬𝐢 𝐊𝐥𝐚𝐬𝐢𝐟𝐢𝐤𝐚𝐬𝐢 𝐓𝐢𝐧𝐠𝐤𝐚𝐭 𝐊𝐞𝐦𝐢𝐬𝐤𝐢𝐧𝐚𝐧 𝐝𝐢 𝐈𝐧𝐝𝐨𝐧𝐞𝐬𝐢𝐚

Sebuah mini-proyek berbasis **FastAPI** untuk memprediksi **tingkat klasifikasi kemiskinan berdasarkan indikator sosial ekonomi di Indonesia.**

## 📁 𝐒𝐭𝐫𝐮𝐤𝐭𝐮𝐫 𝐅𝐢𝐥𝐞

```
├── app_final.py             # Endpoint API utama
├── model.pkl                # File model Decision Tree yang telah dilatih
├── test_predict_clean.http  # File testing API menggunakan REST Client
├── requirements.txt         # Daftar dependency yang dibutuhkan
```

## 🚀 𝐅𝐢𝐭𝐮𝐫 𝐀𝐏𝐈

- Prediksi klasifikasi tingkat kemiskinan.
- Menerima input melalui metode POST (10 fitur sosial ekonomi).
- Output prediksi: kategori klasifikasi kemiskinan.
- Ringan, cepat, dan siap diintegrasikan dengan aplikasi lain.

## ⚙️ 𝐂𝐚𝐫𝐚 𝐌𝐞𝐧𝐣𝐚𝐥𝐚𝐧𝐤𝐚𝐧

### 𝟏. 𝐏𝐚𝐬𝐭𝐢𝐤𝐚𝐧 𝐒𝐮𝐝𝐚𝐡 𝐈𝐧𝐬𝐭𝐚𝐥𝐥 𝐏𝐚𝐜𝐤𝐚𝐠𝐞

```
pip install fastapi uvicorn scikit-learn joblib
```

### 𝟐. 𝐉𝐚𝐥𝐚𝐧𝐤𝐚𝐧 𝐀𝐏𝐈
```
uvicorn app_final:app --reload
```
### 𝟑. 𝐀𝐤𝐬𝐞𝐬 𝐃𝐨𝐤𝐮𝐦𝐞𝐧𝐭𝐚𝐬𝐢 𝐀𝐏𝐈

Buka browser ke:
	•	http://127.0.0.1:8000/redoc → (otomatis redirect ke Redoc)
	•	http://127.0.0.1:8000/docs → (Swagger UI)

 ## 🧪 𝐂𝐨𝐧𝐭𝐨𝐡 𝐉𝐒𝐎𝐍 𝐈𝐧𝐩𝐮𝐭

 ```{
  "rata_rata_lama_sekolah": 8.5,
  "pengeluaran_perkapita": 2500000,
  "indeks_pembangunan_manusia": 72.5,
  "akses_sanitasi": 85.0,
  "akses_air_minum": 90.0,
  "tingkat_pengangguran_terbuka": 6.5,
  "tingkat_partisipasi_angkatan_kerja": 67.0,
  "pdrb": 15000000,
  "persentase_penduduk_miskin": 10.5,
  "pertumbuhan_ekonomi": 5.1
}
```

## ✅ 𝐂𝐨𝐧𝐭𝐨𝐡 𝐎𝐮𝐭𝐩𝐮𝐭

```{
  "prediction_result": "Miskin",
  "input_data": {
    ...
  }
}
```

## 📚 𝐂𝐚𝐭𝐚𝐭𝐚𝐧

Proyek ini dibuat sebagai bagian dari tahapan Deployment model Machine Learning berbasis FastAPI.
Dapat dikembangkan lebih lanjut untuk prediksi sosial ekonomi skala nasional.

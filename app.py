from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import joblib
import numpy as np

# Inisialisasi FastAPI
app = FastAPI(
    title="API Prediksi Tingkat Kemiskinan di Indonesia",
    description="API ini digunakan untuk memprediksi klasifikasi tingkat kemiskinan berdasarkan indikator sosial ekonomi.",
    version="1.0"
)

# Load model
model = joblib.load("model.pkl")

# Format input data menggunakan Pydantic (10 fitur)
class PovertyFeatures(BaseModel):
    rata_rata_lama_sekolah: float
    pengeluaran_perkapita: float
    indeks_pembangunan_manusia: float
    akses_sanitasi: float
    akses_air_minum: float
    tingkat_pengangguran_terbuka: float
    tingkat_partisipasi_angkatan_kerja: float
    pdrb: float
    persentase_penduduk_miskin: float
    pertumbuhan_ekonomi: float

# Redirect root ke Redoc documentation
@app.get("/", include_in_schema=False)
def redirect_to_redoc():
    return RedirectResponse(url="/redoc")

# Endpoint prediksi
@app.post("/predict", summary="Prediksi Tingkat Kemiskinan", tags=["Prediction"])
def predict(data: PovertyFeatures):
    input_array = np.array([
        data.rata_rata_lama_sekolah,
        data.pengeluaran_perkapita,
        data.indeks_pembangunan_manusia,
        data.akses_sanitasi,
        data.akses_air_minum,
        data.tingkat_pengangguran_terbuka,
        data.tingkat_partisipasi_angkatan_kerja,
        data.pdrb,
        data.persentase_penduduk_miskin,
        data.pertumbuhan_ekonomi
    ]).reshape(1, -1)

    prediction = model.predict(input_array)

    return {
        "prediction_result": prediction.tolist()[0],
        "input_data": data.dict()
    }

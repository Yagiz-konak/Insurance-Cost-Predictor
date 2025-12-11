# 🏥 Insurance Cost Prediction - Sigorta Maliyeti Tahmin Uygulaması

Machine Learning tabanlı sigorta maliyeti tahmin uygulaması. LightGBM algoritması kullanılarak eğitilmiş model ile kişisel bilgilere göre yıllık sigorta maliyeti tahmini yapar.

## 📊 Proje Hakkında

Bu proje, yaş, cinsiyet, BMI, çocuk sayısı, sigara kullanımı ve bölge bilgilerine dayanarak bir kişinin yıllık sigorta maliyetini tahmin eder. Modern bir web arayüzü ile kullanıcı dostu bir deneyim sunar.

### 🎯 Model Performansı

- **R² Skoru:** %87.58
- **RMSE:** $4,390.76
- **MAE:** $2,484.31
- **Algoritma:** LightGBM (Gradient Boosting)

## 🚀 Teknolojiler

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Machine Learning:** LightGBM, Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Model Persistence:** Joblib

## 📋 Özellikler

- ✅ Gerçek zamanlı tahmin
- ✅ Modern ve kullanıcı dostu arayüz
- ✅ Risk faktörü analizi
- ✅ Aylık maliyet hesaplama
- ✅ Backend durum kontrolü
- ✅ Responsive tasarım

## 🛠️ Kurulum

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/kullaniciadi/InsuranceML.git
cd InsuranceML
```

### 2. Sanal Ortam Oluşturun (Opsiyonel ama Önerilen)

```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

## 🎮 Kullanım

Uygulamayı çalıştırmak için **iki terminal** açmanız gerekir:

### Terminal 1: Backend (FastAPI)

```bash
uvicorn main:app --reload
```

Backend şu adreste çalışacak: **http://localhost:8000**

### Terminal 2: Frontend (Streamlit)

```bash
streamlit run app.py
```

Frontend şu adreste çalışacak: **http://localhost:8501**

Tarayıcınızda otomatik olarak açılacaktır.

## 📁 Proje Yapısı

```
InsuranceML/
├── app.py                 # Streamlit frontend uygulaması
├── main.py                # FastAPI backend API
├── Model.ipynb            # Model eğitimi ve analiz notebook'u
├── final_model.pkl        # Eğitilmiş LightGBM modeli
├── insurance.csv          # Eğitim veri seti
├── requirements.txt       # Python bağımlılıkları
├── .gitignore            # Git ignore dosyası
└── README.md             # Proje dokümantasyonu
```

## 📊 Veri Seti

Veri seti aşağıdaki özellikleri içerir:

| Özellik   | Açıklama                        | Tip       |
|-----------|---------------------------------|-----------|
| age       | Yaş (18-100)                    | Integer   |
| sex       | Cinsiyet (male/female)          | String    |
| bmi       | Vücut Kitle İndeksi             | Float     |
| children  | Çocuk sayısı (0-10)             | Integer   |
| smoker    | Sigara kullanımı (yes/no)       | String    |
| region    | Bölge (northeast, northwest,... | String    |
| charges   | Yıllık sigorta maliyeti (hedef) | Float     |

## 🔧 API Kullanımı

### Tahmin Endpoint'i

**POST** `/predict`

**Request Body:**
```json
{
  "age": 30,
  "sex": "male",
  "bmi": 25.5,
  "children": 2,
  "smoker": "no",
  "region": "southwest"
}
```

**Response:**
```json
{
  "prediction": 4500.25
}
```

### Sağlık Kontrolü

**GET** `/`

**Response:**
```json
{
  "message": "Hello World"
}
```

## 📈 Model Eğitimi

Model eğitimi ve analizi için `Model.ipynb` notebook dosyasını inceleyebilirsiniz. Notebook şunları içerir:

- Veri keşfi ve görselleştirme
- Veri temizleme ve ön işleme
- Feature engineering
- Model eğitimi ve hiperparametre ayarlama
- Model değerlendirme ve karşılaştırma

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje eğitim amaçlı oluşturulmuştur.

## ⚠️ Uyarı

Bu uygulama sadece tahmin ve eğitim amaçlıdır. Gerçek sigorta fiyatlandırması için profesyonel bir sigortacıya danışmanız önerilir.

## 📧 İletişim

Sorularınız için issue açabilir veya pull request gönderebilirsiniz.

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

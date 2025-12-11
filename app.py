import streamlit as st
import requests
import json

# Sayfa yapılandırması
st.set_page_config(
    page_title="Sigorta Maliyeti Tahmin",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS ile özel stil
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .info-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 1rem 0;
    }
    h1 {
        color: #1f2937;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# API URL
API_URL = "http://localhost:8000"

# API bağlantı kontrolü
def check_api_connection():
    try:
        response = requests.get(f"{API_URL}/", timeout=2)
        return response.status_code == 200
    except:
        return False

# Tahmin API'sine istek gönder
def get_prediction(data):
    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Hatası: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        st.error("❌ Backend'e bağlanılamadı! Lütfen FastAPI sunucusunun çalıştığından emin olun.")
        st.info("💡 Terminalde şu komutu çalıştırın: `uvicorn main:app --reload`")
        return None
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
        return None

# Ana başlık
st.title("🏥 Sigorta Maliyeti Tahmin Uygulaması")
st.markdown("---")

# Sidebar - Bilgilendirme
with st.sidebar:
    st.header("📊 Model Hakkında")
    st.markdown("""
    <div class='info-box'>
    <h4>Model Performansı</h4>
    <ul>
        <li>🎯 <b>R² Skoru:</b> %87.58</li>
        <li>📉 <b>RMSE:</b> $4,390.76</li>
        <li>📊 <b>MAE:</b> $2,484.31</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
    <h4>Kullanılan Özellikler</h4>
    <ul>
        <li>Yaş</li>
        <li>Cinsiyet</li>
        <li>Vücut Kitle İndeksi (BMI)</li>
        <li>Çocuk Sayısı</li>
        <li>Sigara Kullanımı</li>
        <li>Bölge</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Model, LightGBM algoritması kullanılarak eğitilmiştir.")
    
    # API durum kontrolü
    st.markdown("---")
    st.subheader("🔌 Backend Durumu")
    if check_api_connection():
        st.success("✅ Backend bağlantısı başarılı")
    else:
        st.error("❌ Backend'e bağlanılamıyor")
        st.code("uvicorn main:app --reload", language="bash")

# Ana içerik alanı
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Kişisel Bilgilerinizi Girin")
    
    # Form oluşturma
    with st.form("prediction_form"):
        # İki sütunlu form
        form_col1, form_col2 = st.columns(2)
        
        with form_col1:
            age = st.number_input(
                "🎂 Yaş",
                min_value=18,
                max_value=100,
                value=30,
                help="Lütfen yaşınızı girin (18-100 arası)"
            )
            
            sex = st.selectbox(
                "👤 Cinsiyet",
                options=["male", "female"],
                format_func=lambda x: "Erkek" if x == "male" else "Kadın"
            )
            
            bmi = st.number_input(
                "⚖️ Vücut Kitle İndeksi (BMI)",
                min_value=10.0,
                max_value=60.0,
                value=25.0,
                step=0.1,
                help="BMI = Kilo(kg) / Boy(m)²"
            )
        
        with form_col2:
            children = st.number_input(
                "👶 Çocuk Sayısı",
                min_value=0,
                max_value=10,
                value=0,
                help="Bakmakla yükümlü olduğunuz çocuk sayısı"
            )
            
            smoker = st.selectbox(
                "🚬 Sigara Kullanımı",
                options=["no", "yes"],
                format_func=lambda x: "Hayır" if x == "no" else "Evet"
            )
            
            region = st.selectbox(
                "📍 Bölge",
                options=["southwest", "southeast", "northwest", "northeast"],
                format_func=lambda x: {
                    "southwest": "Güneybatı",
                    "southeast": "Güneydoğu",
                    "northwest": "Kuzeybatı",
                    "northeast": "Kuzeydoğu"
                }[x]
            )
        
        # Tahmin butonu
        submit_button = st.form_submit_button("🔮 Maliyeti Tahmin Et")

with col2:
    st.header("💰 Tahmin Sonucu")
    
    if submit_button:
        # Veri hazırlama
        input_data = {
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region
        }
        
        # API'ye istek gönder
        with st.spinner('Tahmin yapılıyor...'):
            result = get_prediction(input_data)
        
        if result and 'prediction' in result:
            prediction = result['prediction']
            
            # Sonucu gösterme
            st.markdown(f"""
                <div class='prediction-box'>
                    <h2>Tahmini Yıllık Sigorta Maliyeti</h2>
                    <h1 style='font-size: 3rem; margin: 1rem 0;'>${prediction:,.2f}</h1>
                    <p style='font-size: 1.1rem; opacity: 0.9;'>Model güven skoru: %87.58</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Aylık maliyet hesaplama
            monthly_cost = prediction / 12
            st.markdown(f"""
                <div class='metric-card'>
                    <h3 style='color: #667eea; margin-bottom: 0.5rem;'>📅 Aylık Maliyet</h3>
                    <h2 style='color: #1f2937;'>${monthly_cost:,.2f}</h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Risk faktörleri analizi
            st.markdown("### 📊 Risk Faktörleri")
            risk_factors = []
            
            if smoker == "yes":
                risk_factors.append("🔴 Sigara kullanımı maliyeti önemli ölçüde artırır")
            
            if bmi > 30:
                risk_factors.append("🟡 Yüksek BMI değeri")
            elif bmi < 18.5:
                risk_factors.append("🟡 Düşük BMI değeri")
            
            if age > 50:
                risk_factors.append("🟡 50 yaş üstü")
            
            if len(risk_factors) > 0:
                for factor in risk_factors:
                    st.warning(factor)
            else:
                st.success("✅ Düşük risk profili")

# Alt bilgi
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #6b7280; padding: 1rem;'>
        <p>⚠️ Bu tahmin sadece referans amaçlıdır ve kesin bir fiyat garantisi değildir.</p>
        <p>🔐 Verileriniz güvenlidir ve hiçbir yerde saklanmamaktadır.</p>
    </div>
""", unsafe_allow_html=True)

# Nasıl kullanılır açıklaması (eğer backend çalışmıyorsa)
if not check_api_connection():
    st.markdown("---")
    st.warning("### ⚠️ Backend Başlatma Talimatları")
    st.markdown("""
    Uygulamayı kullanabilmek için önce backend'i başlatmanız gerekiyor:
    
    **Adım 1:** Yeni bir terminal açın
    
    **Adım 2:** Aşağıdaki komutu çalıştırın:
    ```bash
    uvicorn main:app --reload
    ```
    
    **Adım 3:** Backend başladıktan sonra bu sayfayı yenileyin
    """)


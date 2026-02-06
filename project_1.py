import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def projek1():
    st.title('📊 RFM Analysis on Indian Bank')
    df = pd.read_csv('bank_transactions.csv')

    st.subheader('Data Preview')
    st.dataframe(df.head())
    st.subheader('📊 Top 5 Cities by Total Sales')
    
    sales_location = (
    df.groupby("CustLocation")["TransactionAmount (INR)"]
    .sum()
    .reset_index()
    .sort_values(by="TransactionAmount (INR)", ascending=False)
    .head(5)
    )

    st.dataframe(sales_location)

    st.bar_chart(
    sales_location.set_index("CustLocation")["TransactionAmount (INR)"]
    )

    st.markdown("""
### 🔍 Insight
- Hanya **5 kota teratas** yang menyumbang porsi terbesar dari total transaksi
- Kota dengan transaksi tertinggi berpotensi menjadi **prioritas strategi bisnis**
- Fokus pada kota ini dapat meningkatkan efisiensi pemasaran dan layanan
""")
    
    df1= pd.read_csv('RFMFINRO_Analysis.csv')
    st.subheader('👥 Customer Segmentation Overview')
    segment_count =(
    df1['Segment']
    .value_counts()
    .reset_index()
    )

    segment_count.columns = ['Segment', 'Total Customers']

    st.write("📊 Number of Customers per Segment")
    st.dataframe(segment_count)

    st.bar_chart(
    segment_count.set_index("Segment")["Total Customers"]
    )


    st.subheader("👥 Customer Segmentation (RFM) – Business Explanation")

    segments = {
    "Champions": {
        "desc": "Customer paling bernilai dengan aktivitas tinggi dan transaksi terbaru.",
        "strategy": [
            "Loyalty eksklusif",
            "Priority service",
            "Retensi jangka panjang"
        ]
    },
    "Loyal Customers": {
        "desc": "Customer setia dengan frekuensi transaksi konsisten.",
        "strategy": [
            "Program loyalti",
            "Reward berbasis aktivitas",
            "Upselling ringan"
        ]
    },
    "Potential Loyalist": {
        "desc": "Customer dengan potensi tinggi untuk menjadi loyal.",
        "strategy": [
            "Personalized promotion",
            "Cross-selling",
            "Edukasi produk"
        ]
    },
    "New/Promising": {
        "desc": "Customer baru dengan aktivitas transaksi terbaru.",
        "strategy": [
            "Welcome campaign",
            "Onboarding",
            "First-purchase incentive"
        ]
    },
    "Need Attention": {
        "desc": "Customer yang mulai menunjukkan penurunan aktivitas.",
        "strategy": [
            "Reminder",
            "Re-engagement campaign",
            "Follow-up personal"
        ]
    },
    "At Risk": {
        "desc": "Customer bernilai yang sudah lama tidak bertransaksi.",
        "strategy": [
            "Win-back campaign",
            "Limited-time offer",
            "Survey feedback"
        ]
    },
    "Hibernating": {
        "desc": "Customer lama dengan kontribusi rendah.",
        "strategy": [
            "Low-cost marketing",
            "Re-engagement ringan",
            "Tidak jadi prioritas"
        ]
    }
        }

    selected_segment = st.selectbox(
    "📌 Pilih Segment Customer",
    list(segments.keys())
    )

    st.subheader(f"🔍 {selected_segment}")

    st.write(segments[selected_segment]["desc"])

    st.markdown("### 🎯 Recommended Business Strategy")
    for s in segments[selected_segment]["strategy"]:
        st.markdown(f"- {s}")

  
    st.subheader("""
📈 Recommended Action Plan
- Prioritaskan **loyalty program** untuk Champions di top cities
- Jalankan **personalized promotion** untuk Potential Loyalist di kota utama
- Alokasikan budget marketing berdasarkan **segment + lokasi**
""")
    st.success('''👉 **Prediksi Bisnis:**
Jika perusahaan memfokuskan strategi **retensi dan upselling customer bernilai tinggi**
di **5 kota dengan total sales terbesar**, maka potensi peningkatan revenue akan
lebih optimal dibanding strategi yang bersifat general.''')
    

                





    
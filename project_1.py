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

    st.subheader("📊 Number of Customers per Segment")
    st.dataframe(segment_count)

    st.bar_chart(
    segment_count.set_index("Segment")["Total Customers"]
    )

    st.markdown("""
    ### 👑 Champions
- Customer paling bernilai dengan **frekuensi dan monetary tertinggi**
- Kontributor utama terhadap total revenue  

**Action:**
- Program loyalty eksklusif  
- Retensi dan engagement jangka panjang  

---

### 🌟 Potential Loyalist
- Customer dengan potensi tinggi untuk menjadi Champions  
- Frekuensi transaksi stabil dan monetary menengah–tinggi  

**Action:**
- Personalized promotion  
- Upselling & cross-selling  

---

### 🆕 New / Promising
- Customer baru dengan aktivitas transaksi terbaru  
- Masih memiliki frekuensi dan monetary rendah  

**Action:**
                - Welcome campaign  
- Edukasi produk dan onboarding  

---

### ⚠️ At Risk
- Customer dengan riwayat transaksi baik namun sudah lama tidak aktif  
- Berisiko tinggi churn  

**Action:**
- Win-back campaign  
- Reminder & limited-time offer  

---
### 🧊 Low Value / Hibernating
- Kontribusi revenue rendah  
- Tidak menjadi prioritas utama  

**Action:**
- Low-cost marketing  
- Re-engagement ringan  
""")
    
    st.success("""
### 📈 Recommended Action Plan
- Prioritaskan **loyalty program** untuk Champions di top cities
- Jalankan **personalized promotion** untuk Potential Loyalist di kota utama
- Alokasikan budget marketing berdasarkan **segment + lokasi**
""")

                





    
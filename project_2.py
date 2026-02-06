import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def projek2():
    st.title('📊 Data Scrapping from Jobstreet')
    st.image('jobstreet.png')
    st.subheader("""
Telah dilakukan **web scraping lowongan Data Analyst dari JobStreet Indonesia** menggunakan **BeautifulSoup**.
""")
    
    df = pd.read_csv('data_general_clean.csv')
    st.subheader('Data Preview')
    st.dataframe(df.head())

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Lowongan", df.shape[0])
    col2.metric("Total Perusahaan", df["company"].nunique())
    col3.metric("Rata-rata Gaji", f"Rp {int(df['salary'].mean()):,}")
    
    st.divider()
    
    fcol1, fcol2 = st.columns(2)

    with fcol1:
        selected_location = st.multiselect(
        "Pilih Lokasi",
        options=sorted(df["location"].unique()),
        default=sorted(df["location"].unique())
        )

    with fcol2:
        min_salary, max_salary = st.slider(
        "Range Gaji",
        min_value=int(df["salary"].min()),
        max_value=int(df["salary"].max()),
        value=(int(df["salary"].min()), int(df["salary"].max()))
        )

    filtered_df = df[
    (df["location"].isin(selected_location)) &
    (df["salary"].between(min_salary, max_salary))
    ]

    st.divider()

    st.subheader("📋 Data Lowongan (Hasil Filter)")
    st.dataframe(
    filtered_df[["title", "company", "location", "salary", "posted"]],
    use_container_width=True
    )    

    st.subheader("📍 Top 10 Lokasi Lowongan")

    location_count = (
        filtered_df["location"]
        .value_counts()
        .head(10)
        )
    fig1, ax1 = plt.subplots()
    location_count.plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Lokasi")
    ax1.set_ylabel("Jumlah Lowongan")
    st.pyplot(fig1)
    
    st.subheader("📌 Insight")

    if not filtered_df.empty :
        top_location = location_count.index[0]
        avg_salary = int(filtered_df["salary"].mean())
        st.markdown(f"""
    - Lokasi dengan lowongan terbanyak: **{top_location}**
    - Rata-rata gaji Data Analyst: **Rp {avg_salary:,}**
    - Lowongan terkonsentrasi di kota besar dan pusat bisnis
    """)
    else :
        st.warning("Tidak ada data yang sesuai dengan filter.")

        

    



    
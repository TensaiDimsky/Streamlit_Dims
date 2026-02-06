import streamlit as st

def aboutme():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('17709cf5-94f5-4cd3-bc20-1e68241f6a9c.jpg', width=200)
    with col2:
        st.header('📄 About Me')
        st.write("""
I am a **Data Analyst**, based in jakarta, who is interested in:
- Data-driven decision making
- Business analytics
- Customer behavior analysis
""")
        st.markdown("""
📧 **Email:** wibisonopanji4@gmail.com  
💼 **LinkedIn:** linkedin.com/in/dimaswibisono  
🐙 **GitHub:** github.com/tensaidimsky
""")
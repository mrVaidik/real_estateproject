import streamlit as st
video_01 = open('01.mp4', 'rb')
video_1 = video_01.read()

video_02 = open('02.mp4', 'rb')
video_2 = video_02.read()

video_03 = open('03.mp4', 'rb')
video_3 = video_03.read()



st.set_page_config(
    page_title='Home',
    page_icon=':',
)
st.title("")
st.sidebar.success("")

st.title("""
         
Welcome to Real Estate Price Predictor 
         """)

st.divider()

st.markdown("""
            
- Introducing the Real Estate Price Predictor, the go-to solution for precise property evaluations. Whether you're a seller, buyer, or real estate professional, our platform provides accurate and insightful market analysis tailored to your specific needs. This model based on Gurugram city house&flats Datasets.           
    
# Price Predictor For Property  
- 
  
      
            """)

st.video(video_1)

st.markdown("""
            
- ### Accurate Estimates 
  Our advanced algorithm analyzes various factors such as location, property size, amenities, and market trends to provide accurate price predictions for any property.
- ### Comprehensive Data 
  Leveraging big datasets and cutting-edge machine learning techniques, our model delivers reliable price estimates to help you make informed decisions.
  

            """)
st.divider()
st.markdown("""
 #  Find Similar Properties 
            """)
st.video(video_3)
st.markdown("""
            
- ### Comparable Listings
   Discover properties similar to your input property within the same neighborhood or city. Compare features, prices, and other key metrics to understand the market better.

            """)

st.divider()
st.markdown("""
            #  Properties Near Public Places
            """)

st.video(video_2)

st.markdown("""

- ### Nearby Amenities
    Explore properties located near public places such as parks, schools, hospitals, and transportation hubs. Easily identify properties with convenient access to essential amenities.  
            """)

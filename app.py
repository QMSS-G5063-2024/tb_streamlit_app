import streamlit as st
import numpy as np
import pandas as pd
import time

st.header("Our first streamlit app!")
textinput = st.text_input('Enter some text')
st.write(textinput)


exit()

# Here are the functions we want to try out

# Display Text
st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# User input
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)

# Magic commands
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

# Data Table
import numpy as np
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

## Highlight
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

## Static Table
st.table(dataframe)

## Line Chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
chart_data
st.line_chart(chart_data)

## Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Simple Widgets
st.button('Click me')
st.checkbox('Check me out')
st.radio('Choose one', ['Option A', 'Option B', 'Option C'])
st.selectbox('Choose an option', ['Option 1', 'Option 2', 'Option 3'])
st.multiselect('Pick your favorite colors', ['Green', 'Yellow', 'Red', 'Blue'])
st.slider('Select a range', 0, 100, (25, 75))
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Select a date')
st.time_input('Select a time')
st.file_uploader('Upload a file')
st.color_picker('Pick a color')

## Expander
with st.expander("See details"):
    st.write("Here you can put in detailed information.")

## Progress bar
import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i+1)

## Spinner
with st.spinner('Wait for it...'):
    time.sleep(5)
    st.success('Done!')

## Ballons
st.balloons()

## Camera input
image = st.camera_input("Take a picture")

## Metric
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

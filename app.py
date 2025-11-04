import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title("Flights Analytics")

user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title("Check Flights")
    col1, col2 = st.columns(2)
    city = db.fetch_city_names()

    with col1:
        source = st.selectbox('Source', sorted(city))

    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        result = db.fetch_all_flights(source, destination)
        st.dataframe(result)

elif user_option == 'Analytics':
    # Pie Chart for Airlines
    airline, frequency = db.fetch_airline_data()
    pie_fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )

    st.header("Airline Frequency (Pie Chart)")
    st.plotly_chart(pie_fig, use_container_width=True)

    # Bar Chart for Busiest Airports
    city, frequency1 = db.busy_airport()
    bar_fig = px.bar(
        x=city,
        y=frequency1,
        title='Busiest Airports',
        labels={'x': 'City', 'y': 'Flight Frequency'},
        color=city  # optional: gives each bar a unique color
    )

    st.header("Busiest Airports (Bar Chart)")
    st.plotly_chart(bar_fig, use_container_width=True)

else:
    st.title("Tell us about this Project")

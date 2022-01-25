import streamlit as st

total = st.number_input("Enter number of bananas at starting:",
                        min_value=10, max_value=10000, value=3000, step=10)
distance = st.slider('Enter the distance you want to cover: ', 0, 10, 10000)
capacity = st.number_input(
    'Enter the Maximum capacity of your camel:', min_value=1, max_value=10000, value=1000, step=10)


def meth():
    lose = 0
    start = total
    for i in range(distance):
        while start > 0:
            start = start-capacity

            if start == 1:
                lose = lose-1
            lose = lose+2

        lose = lose-1
        start = total-lose
        if start == 0:
            break
    st.write(
        f"The maximum number of bananas that can be transferred to the destination using only camel: {start}")


st.button("Calculate", on_click=meth)

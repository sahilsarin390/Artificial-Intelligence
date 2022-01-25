import streamlit as st

st.markdown('''
    # Toy Problem
    ___
    A person has 3000 bananas and a camel. The person wants to transport the
    maximum number of bananas to a destination which is 1000 KMs away, using only
    the camel as a mode of transportation. The camel cannot carry more than 1000
    bananas at a time and eats a banana every km it travels. What is the maximum
    number of bananas that can be transferred to the destination using only a camel (no
    other mode of transportation is allowed).
    ___
''')

st.image('camel.png')


total = st.number_input("Enter number of bananas at starting:",
                        min_value=10, max_value=10000, value=3000, step=10)
distance = st.slider('Enter the distance you want to cover: ',
                     min_value=10, max_value=10000, value=1000, step=10)
capacity = st.number_input(
    'Enter the Maximum capacity of your camel:', min_value=1, max_value=10000, value=1000, step=10)


with st.container():
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
        st.balloons()
        col1, col2 = st.columns(2)
        st.write(
            f"The maximum number of bananas that can be transferred to the destination using only camel: {start}", use_column_width=True)

st.button("Calculate", on_click=meth)

import streamlit as st
from recommender_functions import *
from recommender import Recommender
import pickle
from pathlib import Path


rec = Recommender()


def main():
    body()
    sidebar()

def body():
    st.title("Movie Recommendation App")
    st.markdown(
        """
       This application recommends movie to users.
        """, unsafe_allow_html=True)

def sidebar():

    my_file = Path("rec_2")
    if my_file.is_file():
        file = open("rec_2",'rb')
        model_file = pickle.load(file)

    else:   
        rec.fit(reviews_pth='train_data.csv', movies_pth= 'movies_clean.csv', learning_rate=.01, iters=20)
        # Pickling the model
        picklefile = open('rec_2', 'wb')
        pickle.dump(rec, picklefile)
        picklefile.close()
        file = open("rec_2",'rb')
        model_file = pickle.load(file)

    if model_file:
        type = ["movie", "user"]
        deselect = list(set(type))
        num_users = st.sidebar.markdown("Total users:" + str(model_file.n_users))
        num_movies = st.sidebar.markdown("Total movies:" + str(model_file.n_movies))
        activity = st.sidebar.selectbox("What do you want to perform?", deselect)
        if 'user' in activity:
            user_id = st.sidebar.text_input("Enter the user_id")

        else:
            user_id = st.sidebar.text_input("Enter the user_id")
            movie_name = model_file.helper_function(user_id)
            movie_name = st.sidebar.markdown("Movie Name:" + str(movie_name))
        
        if st.sidebar.button("Recommendations"):
            val = model_file.make_recommendations(int(user_id), activity)
            ini = 1
            message = val[2]
            if message != None:
                st.write(message)
            
            if val[1] != None:
                for i in val[1]:
                    st.write(str(ini) + '.'  + i)
                    ini += 1
    
    else:
        st.write("Load the model")


if __name__=='__main__':

    main()

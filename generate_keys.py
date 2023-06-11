import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# List of the people who have access to the App
names = ["Snehaunshu","Majid","Husam","Aaryan","Drashti","Sai","Keane","Marshal","Sanjay"]
usernames = ["Snehaunshu","Majid","Husam","Aaryan","Drashti","Sai","Keane","Marshal","Sanjay"]
passwords = ["Snehaunshu","Majid","Husam","Aaryan","Drashti","Sai","Keane","Marshal","Sanjay"]
hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

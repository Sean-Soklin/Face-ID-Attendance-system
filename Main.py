# Main code for attendance project
# library 

import pickle
import sys

try:
    with open("encodings.pickle", "rb") as file:
        data = pickle.load(file)

    knownEncodings = data["encodings"]
    knownNames = data["names"]

except FileNotFoundError:
    print("Error: encodings.pickle file not found.")
    sys.exit()

markedStudents = set()



# 2. camera handle and face recognition handle (Nimol , Nynich)



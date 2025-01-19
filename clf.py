import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle


clf = pickle.load(open('clf.pkl', 'rb'))
categorical_columns = pickle.load(open('financial_inclusion.pkl', 'rb'))

def prediction(data):
    le = LabelEncoder()
    df = pd.DataFrame(data)


    for col in data:
        if type(col) == str:
            #df[col] = le.transform([df[col][0]])
            df.iloc[data.index(col)] = le.fit_transform(df.iloc[data.index(col)])



    pred = clf.predict(df.values.reshape(1,-1))

    if pred[0] == 1:
        return "This individual is likely to have or use a bank account."
    else:
        return "This individual is not likely to have to have or use a bank account."


print(prediction(['Kenya', 2018,'uniqueid_4','Rural','Yes',5, 34,'Female','Head of Household',
                  'Married/Living together','Primary education','Formally employed Private']))
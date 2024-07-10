import pandas as pd   
import numpy as np     
import matplotlib as plt    
import seaborn as sns    
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import pickle

df= pd.read_csv(r"C:\Users\priyankd3\Desktop\ML project\diabetes_prediction_dataset.csv")

#EDA
# sns.barplot(x="heart_disease",y="smoking_history",data=df)   
df["gender"]= df["gender"].map({"Male":1,"Female":0,"Other":2})
df.drop(["smoking_history"],axis=1,inplace=True)
#split the data 
X=df.drop(["diabetes"],axis=1)
Y=df["diabetes"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,stratify=Y,random_state=30,test_size=.2)

scale=MinMaxScaler()
X_train_scale=scale.fit_transform(X_train)
X_test_scale=scale.fit_transform(X_test)
# print(X.isnull().sum())

KNN=KNeighborsClassifier()
KNN.fit(X_train_scale,Y_train)

pred=KNN.predict(X_test_scale)

classifiction=classification_report(Y_test,pred)
accuracy=accuracy_score(Y_test,pred)
confusion=confusion_matrix(Y_test,pred)
pickel_open=open("KNN.pkl","wb")
pickle.dump(KNN,pickel_open)
pickel_open.close()

# print(classifiction)
# print(accuracy)
# print(confusion)


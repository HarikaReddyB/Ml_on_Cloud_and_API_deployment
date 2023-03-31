# Importing the libraries
import pandas as pd
import pickle

dataset = pd.read_csv('https://raw.githubusercontent.com/HarikaReddyB/Flask_deployment/main/homeprices.csv')

dataset = dataset[['area', 'bedrooms', 'age', 'price']]

# Replacing missing values
dataset['area'].fillna(dataset['area'].mean(), inplace=True)
dataset['bedrooms'].fillna(0, inplace=True)

X = dataset.iloc[:, :3]


y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results of analysis
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2200, 2, 5]]))



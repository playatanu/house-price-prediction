import pandas as pd
from sklearn import linear_model

#price = predict(2000, 0, 0,23.4037,88.3659)
def predict(sqrt,bedrooms,bathrooms,latitude,longitude,houseList) :

    df = pd.DataFrame(houseList)

    df.sqrt = df.sqrt.fillna(df.sqrt.median())
    df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())
    df.bathrooms =  df.bathrooms.fillna(df.bathrooms.median())
    df.price =  df.price.fillna(df.price.median())
    df.latitude = df.latitude.fillna(df.latitude.median())
    df.longitude = df.longitude.fillna(df.longitude.median())

    reg = linear_model.LinearRegression()
    reg.fit(df.drop('price',axis='columns').values,df.price)

    reg.coef_

    reg.intercept_

    price = reg.predict([[sqrt, bedrooms, bathrooms,latitude,longitude]] )
    return price[0].round()








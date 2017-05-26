from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
from sklearn.externals import joblib


if __name__ == "__main__":
        # Load data
        df = pd.read_csv('airbnb_0513_2306.csv')
        cols = ['gender','age','action_search','timestamp_month','timestamp_day','signup_flow']
        for i in cols:
            df[i] = df[i].fillna(df[i].mean())
        #features = df.loc[:,['age', 'gender','signup_flow', 'action_search','action_user_profile','action_update_listing','action_booking_requests', 'action_p5','count','max', 'booking_month','affiliate_provider_craigslist','timestamp_month', 'booking_year','booking_day']]
        features = df.loc[:,['gender','age','action_search','timestamp_month','timestamp_day','signup_flow']]
        target = df.loc[:,'country_destination']
        
        #xgb = XGBClassifier()  # replace with your own ML model here
        #xgb.fit(features, target)
        gbc = GradientBoostingClassifier()  # replace with your own ML model here
        gbc.fit(features, target)



        joblib.dump(gbc, 'models/airbnb.pkl')

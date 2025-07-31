import numpy as np
import pandas as pd
import joblib

def personality(alone, stage_fear, social_event, going, grained, friends, post) -> pd.DataFrame:
 data = [
     {'Time_spent_Alone': alone,
      'Stage_fear': stage_fear,
      'Social_event_attendance': social_event,
      'Going_outside': going,
      'Drained_after_socializing': grained,
      'Friends_circle_size':friends,
      'Post_frequency':post}
 ]

 df = pd.DataFrame(data)


 # Загружаем модель из файла
 model = joblib.load('model_logicticregr.pkl')

 # Получаем вероятности по каждому классу
 predict = model.predict(df)

 df['Personality'] = predict
 df['Personality'] = df['Personality'].replace({True: 'Introvert', False: 'Extrovert'})
 print(df['Personality'])
 return df['Personality']

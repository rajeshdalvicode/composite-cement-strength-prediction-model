# Step2: Data Preprossing and Cleaning
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler
from sklearn.model_selection import train_test_split

def data_preprocessing(df):

  '''
  step1 : Feauter Engemerring and feauter selection
  step2: split the dataset into a indepedend columns and dependent columns i.e.x and y
  step3: split the data into seen and unseen (seendata Train data and unseendata: test data)
  step4: scalling/normalization the data (stanserdScaller,minMaxscaller,RoubestScaler)
  step5: return the seen and unseen data
  '''


  # feauter Engneering: create new feauter based on existing feauter
  df['Water_#to_Cementitious_MaterialsRatio'] = df['Water  (component 4)(kg in a m^3 mixture)'] / (df['Cement (component 1)(kg in a m^3 mixture)']
                                                                                                  + df['Blast Furnace Slag (component 2)(kg in a m^3 mixture)']
                                                                                                  + df['Fly Ash (component 3)(kg in a m^3 mixture)'])

  # step2: split the dataset into x and y
  target_col= 'Concrete compressive strength(MPa, megapascals) '
  X=df.drop(columns=[target_col])
  y=df[target_col]

  # step3: split the dataset into seen (traun data) unseen (test data)
  X_train,X_test,y_train,y_test=train_test_split(X,y,
                                                  test_size=0.3,
                                                  random_state=1)

  # step4:normalization/scaling technnique
  sc=MinMaxScaler()
  X_train=sc.fit_transform(X_train)
  X_test=sc.transform(X_test)
  return X_train,X_test,y_train,y_test




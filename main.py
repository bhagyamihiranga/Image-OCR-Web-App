from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer



data_set = ['Pass','Pass','Fail','Absent','Pass','Absent','Absent','Fail','Pass','Fail']

#Hot Encoding For Int
obj = LabelEncoder()

result = obj.fit_transform(data_set)


for i,x in zip(data_set,result):
    print(f'{i} : {x}')


print('\n')

#Hot Encoding For Binary


obj2 = LabelBinarizer()

result_binary =obj2.fit_transform(data_set)

print(result_binary
      )

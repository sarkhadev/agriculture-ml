names = ['rice','maize','chickpea','kidneybeans','pigeonpeas','mothbeans','mungbean','blackgram','lentil',
 'pomegranate','banana','mango','grapes','watermelon','muskmelon','apple','orange','papaya','coconut', 
 'cotton','jute','coffee']

encodings = [20,11,3,9,18,13,14,2,10,19,1,12,7,21,15,0,16,17,4,6,8,5]

CropDictionary = {}

for index,encoding in enumerate(encodings):
    CropDictionary[encoding] = names[index]
    
    
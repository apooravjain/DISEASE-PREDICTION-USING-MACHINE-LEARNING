
def Disease_prediction(atr):
    from sklearn.externals import joblib
        
    clf = joblib.load('pickle_model.pkl')
    
    symptoms = atr
    l1 = joblib.load('Symptoms.pkl')
    disease = joblib.load('Disease.pkl')
    
    l2 = joblib.load('list.pkl')
    
    for k in range(0, len(l1)):
            # print (k,)
        for z in symptoms:
            if(z == l1[k]):
                l2[k] = 1
    
    input_ = [l2]
    predict = clf.predict(input_)
    predicted = predict[0]
    
    h = 'no'
    for a in range(0, len(disease)):
        if(predicted == a):
            h = 'yes'
            break
    if h=='yes':
        print(disease[a])
    
    
    return disease[a]
    
#Disease_prediction(atr)
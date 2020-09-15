from flask import Flask, request, render_template
from Validator import Disease_prediction

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Index.html')

@app.route('/DiseasePrediction', methods=['POST'])
def predict():
      
    Name = request.form["Name"]
    Sym1 = request.form["Symptom1"]
    Sym2 = request.form["Symptom2"]
    Sym3 = request.form["Symptom3"]
    Sym4 = request.form["Symptom4"]

    atr = []
    atr.append(Sym1)
    atr.append(Sym2)
    atr.append(Sym3)
    atr.append(Sym4)
        
    prediction = Disease_prediction(atr)
        
    return render_template('response.html', Name=Name, prediction=prediction)

if __name__ == "__main__":
    app.run()


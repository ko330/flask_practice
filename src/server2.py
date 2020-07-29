from flask import Flask,request
app = Flask(__name__)
anomaly=[]
@app.route('/api/alarm',methods=['POST','GET'])
def anomaly_detection():
    if request.method=='GET':
        return str(anomaly)
    data=request.values.to_dict()
    anomaly.append(data)
    print('post',anomaly)
    return 'received'


app.run(port=5001)
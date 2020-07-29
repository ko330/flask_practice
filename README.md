# flask practice
implement anomaly detection with scikit-learn and flask  
data is available in https://github.com/nytimes/covid-19-data/blob/master/us.csv  
assume last 30 days is normal data,  
this project can detect "(date,cases)" is normal or anomaly
## Environment
` pip install -r requirement.txt`

## run servers
`python src/server1.py`
`python src/server2.py`
## send message
`python test/send.py`
you can modify this script or using POSTMAN to send another data   
all anomaly data displayed on http://localhost:5001/api/alarm

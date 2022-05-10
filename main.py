from flask import Flask, render_template, request
from Modules import RequestsServer as rs, crawl_UTE as cu


# create app 
app = Flask(__name__)
# home 
@app.route("/")
def home():
    return render_template("index.html")
# get reply 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    db = request.args.get('DB')
    return rs.main_requests(userText,db)
    

# run main
if __name__ == "__main__":
    cu.crawl_data()
    app.run()
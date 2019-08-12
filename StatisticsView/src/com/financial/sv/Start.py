# from com.financial.statistics.st.OnlyST import OnlyST
# 
# OnlyST().compute()

from flask import Flask
 
from com.financial.sv.views.StatisticsView import sv
 
app = Flask( __name__ )
app.register_blueprint( sv, url_prefix= "/statistics" )
 
if __name__ == '__main__':
    app.run( host = "127.0.0.1", port = "8080", debug = True )
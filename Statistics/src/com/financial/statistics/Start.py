# from com.financial.statistics.st.OnlyST import OnlyST
# 
# OnlyST().compute()

import os
 
from flask import Flask
 
from com.financial.statistics.scheduler import scheduler
from com.financial.statistics.scheduler.SchedulerConfig import SchedulerJobConfig
 
from com.financial.statistics.views.StatisticsView import sv
 
app = Flask( __name__ )
app.config.from_object( SchedulerJobConfig )
app.register_blueprint( sv, url_prefix= "/statistics" )
 
if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN' ) == 'true':
        scheduler.init_app( app )
        scheduler.start()
         
    app.run( host = "127.0.0.1", port = "9090", debug = True )
from flask import Flask

from com.financial.algorithm.view.View001 import view001

app = Flask( __name__ )

app.register_blueprint( view001, url_prefix = "/algorithm/001/" )

if __name__ == '__main__':
    app.run( host = "127.0.0.1", port = "9090", debug = True )
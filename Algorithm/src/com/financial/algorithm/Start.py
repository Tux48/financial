from flask import Flask

from com.financial.algorithm.view.B_001_View import b001

app = Flask( __name__ )

app.register_blueprint( b001, url_prefix = "/algorithm/b001/" )

if __name__ == '__main__':
    app.run( host = "127.0.0.1", port = "9090", debug = True )
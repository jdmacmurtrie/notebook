import routes
from application import app
from flask_cors import CORS


CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(debug=True)

from models.page import Page
from application import app, db
from flask import request

@app.route('/get_pages')
def get_pages():
    pages = db.session.execute(db.select(Page)).scalars().all()
    print(pages)
    response = []

    for page in pages:
        obj = {
            'id': page.id,
            'title': page.title,
            'body': page.body,
        }
        response.append(obj)

    return response

@app.route('/add_page', methods=['POST'])
def add_page():
    data = request.get_json()
    new_page = Page(title=data["title"], body=data['body'])

    db.session.add(new_page)
    db.session.commit()

    return { 'status': 200 }

from demoflask.app import db


class TestMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    methodName = db.Column(db.String(64))
    methodDesc = db.Column(db.String(128))
    className = db.Column(db.String(64))
    classDesc = db.Column(db.String(128))
    fileName = db.Column(db.String(64))
    fileDesc = db.Column(db.String(128))
    moduleName = db.Column(db.String(64))
    moduleDesc = db.Column(db.String(128))
    author = db.Column(db.String(64))
    isSelected = db.Column(db.Boolean, default=False)




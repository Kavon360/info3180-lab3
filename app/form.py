from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email_address = StringField('Email', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    textarea = StringField('Message', validators=[DataRequired()])
    

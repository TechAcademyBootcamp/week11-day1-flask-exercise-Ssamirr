from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired,Length

class BlogForm(FlaskForm):
    title = StringField('Basligi', validators=[Length(min=3, max=255, ), DataRequired()])
    description = TextAreaField('Mezmun', validators=[Length(min=3), DataRequired()])
    # owner_name = StringField('Muellif', validators=[Length(min=3, max=50), DataRequired()])

class ContactForm(FlaskForm):
    username = StringField(validators=[Length(min=3, max=40, ), DataRequired()])
    email = StringField(validators=[Length(min=3, max=40, ), DataRequired()])
    subject = StringField(validators=[Length(min=3, max=255, ), DataRequired()])
    message = TextAreaField(validators=[DataRequired()])

# class AboutWebsite(FlaskForm):
#     social_adress = StringField(validators=[Length(min=3, max=40, ), DataRequired()])
#     email = StringField(validators=[Length(min=3, max=40, ), DataRequired()])
#     phone_number = StringField(validators=[Length(min=3, max=255, ), DataRequired()])

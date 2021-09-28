from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('update your bio for a better feel',validators = [Required()])
    submit = SubmitField('Submit')

class AddBlog(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add comment',validators = [Required()])
    submit = SubmitField('Submit')

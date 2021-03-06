#coding:utf8
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired,EqualTo,Email,Regexp

class UserForm(FlaskForm):
    name = StringField(
        label="account",
        validators=[
            DataRequired("account empty")
        ],
        description="account name",
        render_kw={
            "class": "form-control",
            "placeholder": "input account",
            # "required":"required"
        }
    )
    email=StringField(
        label="email",
        validators=[
            DataRequired("email empty"),
            Email("email format wrong")
        ],
        description="email",
        render_kw={
            "class": "form-control",
            "placeholder": "input email",
            # "required":"required"
        }
    )
    phone=StringField(
        label="phone",
        validators=[
            DataRequired("phone empty"),
            Regexp("\d{10}",message="phone format wrong")
        ],
        description="phone",
        render_kw={
            "class": "form-control",
            "placeholder": "input phone",
            # "required":"required"
        }
    )
    pwd = PasswordField(
        label="password",
        validators=[
            DataRequired("password empty")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "input password",
            # "required": "required"
        }
    )
    r_pwd = PasswordField(
        label="password",
        validators=[
            DataRequired("password empty"),
            EqualTo('pwd',message="password not same")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "input password",
            # "required": "required"
        }
    )
    submit = SubmitField(
        label="signup",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )
class UserInfo(FlaskForm):
    name = StringField(
        label="account",
        description="account name",
        render_kw={
            "class": "form-control",
            "placeholder": "input account",
            # "required":"required"
        }
    )
    email = StringField(
        label="email",
        validators=[
            DataRequired("email empty"),
            Email("email format wrong")
        ],
        description="email",
        render_kw={
            "class": "form-control",
            "placeholder": "input email",
            # "required":"required"
        }
    )
    phone = StringField(
        label="phone",
        validators=[
            DataRequired("phone empty"),
            Regexp("\d{10}", message="phone format wrong")
        ],
        description="phone",
        render_kw={
            "class": "form-control",
            "placeholder": "input phone",
            # "required":"required"
        }
    )
    face=FileField()
    info = TextAreaField(
        label="info",
        validators=[
            DataRequired("info empty")
        ],
        description="info",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    submit = SubmitField(
        label="save",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

class PwdForm(FlaskForm):
    old_pwd=PasswordField(
        label="password",
        validators=[
            DataRequired("password empty")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "input old password",
            # "required": "required"
        }
    )
    new_pwd = PasswordField(
        label="password",
        validators=[
            DataRequired("password empty")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "input new password",
            # "required": "required"
        }
    )
    submit = SubmitField(
        label="change",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )
class CommentForm(FlaskForm):

    info=TextAreaField(
        label="info",
        validators=[
            DataRequired("info empty")
        ],
        description="info",
        render_kw={
            "rows": 10,
            "id":"input_content"
        }
    )
    submit = SubmitField(
        render_kw={
            "class":"btn btn-success",
             "id":"btn-sub"
        }
    )
    # collect = SubmitField(
    #     label="collection",
    #     render_kw={
    #         "class": "btn btn-danger",
    #         "id": "btn-col"
    #     }
    # )

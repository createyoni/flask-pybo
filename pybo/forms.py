from flask_wtf import FlaskForm  # 플라스크 폼
from wtforms import StringField, TextAreaField, PasswordField, EmailField  # 웹상의 폼
from wtforms.validators import DataRequired, Length, EqualTo, Email  # 유효성검사


class QuestionForm(FlaskForm):  # 상속 / 매개변수 아님
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])


class AnswerForm(FlaskForm):  # 상속 / 매개변수 아님
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('사용자이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.'), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired('비밀번호를 확인해주세요')])
    email = EmailField('이메일', [DataRequired('이메일은 필수 입력 항목입니다.'), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('사용자이름을 입력하세요'), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력하세요')])

class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])
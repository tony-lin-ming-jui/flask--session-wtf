from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_wtf import FlaskForm,RecaptchaField#RecaptchaField用於GOOGLE的Recaptcha驗證
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
#生成隨機數的關鍵在於一個好的隨機種子，困此一個好的密鑰應當有足夠的隨機性。
#你的操作系統可以使用一個隨機生成器來生成一個好的隨機種子：

class registlogin(FlaskForm):
    name = StringField(u'用戶名:',validators=[InputRequired(message=u'用戶名未填'),Length(min=3,max=10,message=u'必須輸入3到10個數字或英文字母')])#從這裡取表單的東西,StringField取字串 
    password = PasswordField(u'密碼:',validators=[InputRequired(message=u'密碼未填'),Length(min=4,max=12,message=u'必須輸入4到12個數字或英文字母')])#PasswordField取密碼
    #InputRequired()功能:如果表單未填跳出提醒
    submit = SubmitField(u'登入')


@app.route('/')
def index():
    name = session.get('name')
    return render_template('index.html',name=name)
@app.route('/xxx')
def xxx():
    name = session.get('name')
    return render_template('xxx.html',name=name)

@app.route('/login/',methods=['GET','POST'])
def login():
    form = registlogin()
    #if request.method == 'GET':
        
        #return render_template('login.html',form=form)
    #else:
    if form.validate_on_submit():
        #name = request.form.get('name')
        #password = request.form.get('password')       
        print('name',form.name.data)
        print('password',form.password.data)
        #用字典紀錄登錄登出，真實絕對不會用到的練習
        x={'lin':'1qaz1qaz','smile':'6666'}
        if not x.get(form.name.data):
            print("用戶名錯誤")
            flash(u'用戶名或密碼錯誤')
            #return u'用戶名錯誤'
            return redirect(url_for('login'))
        else:           
            print("用戶名正確")            
            if form.password.data != x[form.name.data]:
                print("密碼錯誤")
                #return u'密碼錯誤'
                flash(u'用戶名或密碼錯誤')
                return redirect(url_for('login'))
            else:
                print("密碼正確")
                session['name']=form.name.data
                return redirect(url_for('index'))
    return render_template('login.html',form=form)        

@app.route('/logout/')
def logout():
        session.clear()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug =True)

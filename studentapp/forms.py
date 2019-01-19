
from django import forms
import mysql.connector


class login(forms.Form):

    school = forms.CharField(label = "Sch Username", max_length= 30, widget= forms.TextInput(attrs= {'placeholder':" Enter School Username"}))
    users = forms.CharField(label = "Username", max_length= 30, widget = forms.TextInput(attrs= {'placeholder':" Username"}))
    passes = forms.CharField(label= "Password", max_length= 30, widget = forms.PasswordInput(attrs= {'placeholder':" Password"}))
    status = forms.CharField(max_length=255)

class bars(forms.Form):
    Term = forms.CharField(max_length=255)
    session = forms.CharField(max_length=255)

    #db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
     #                            host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= school, autocommit = True)
    #cursor = db.cursor()
    #cursor.execute("select CHG_PASSWORD from parent_pass where USERNAME = '%s';" %(users))
    #baa = cursor.fetchall()
    #if baa[0][0] == passes:
     #  pass
    #else:
     #      raise forms.ValidationError(("wrong login details"))

   # def login_pas(self):
    #    username = self.cleaned_data.get("users")
     ##  sch = self.cleaned_data.get("school")


       # db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
          #                       host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= sch.upper(), autocommit = True)
        #cursor = db.cursor()
        #cursor.execute("select CHG_PASSWORD from parent_pass where USERNAME = '%s';" %(username))
        #baa = cursor.fetchall()
        #if baa[0][0] == password:
         #  pass

        #else:
         #  raise forms.ValidationError("wrong login details")
            #form = login()
                #raise form.ValidationError( ("passwords not the same "))

class login_pass(forms.Form):
    school = forms.CharField(label = "Sch Username", max_length= 30, widget= forms.TextInput(attrs= {'placeholder':" Enter School Username"}))
    users = forms.CharField(label = "Username", max_length= 30, widget = forms.TextInput)
    passes = forms.CharField(label= "Password", max_length= 30, widget = forms.PasswordInput)
    chg_pass = forms.CharField(label = "New Password", max_length= 30 , widget = forms.PasswordInput)
    con_pass = forms.CharField(label= "Confirm Password", max_length= 30, widget = forms.PasswordInput)



class SignUpForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)

    #def __init__(self, *args, **kargs):
      #  super(SignUpForm, self).__init__(*args, **kargs)

    ##class Meta:
    #    model = User
    #    fields = '__all__
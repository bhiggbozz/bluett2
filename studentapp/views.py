from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import mysql.connector
from .forms import login, SignUpForm, login_pass, bars
from django.contrib import messages
from base64 import b64decode, b64encode

from django.core.files.storage import default_storage as storage
import binascii
import os

import struct

from django.core.files.base import ContentFile

from django.contrib import messages
forr = {}
parent = 0
bo = []
sess = '2017/2018'
img = {}
sch = ''
goo = {}
info = {}
def index(request):
    #return HttpResponse('<h1> The Home Page </h1>')
   # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('studentapp/home.html')
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'studentapp/index.html')
    return HttpResponse(template.render())

    #return HttpResponse(template.render(context, request))

    #return HttpResponse("Welcome to bluett")
def detail(request, question_id):
    return HttpResponse("you are looking at the question {}".format(question_id))
def detail2(request):
    return HttpResponse("<h1> you are looking at the question </h1>")
def results(request, question_id):
    return HttpResponse("you are looking at the result of the question {}".format(question_id))
def vote(request, question_id):
    return HttpResponse("you are voting for question {}".format(question_id))
db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= "root", autocommit = True)
db.connect()

@csrf_exempt
def pass_input(request):
    username = request.POST['username']
    passes = request.POST['password']
    sch = request.POST['schname']

    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                              host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database=sch, autocommit = True)
    cursor = db.cursor()
    cursor.execute("select CHG_USERNAME from pass_table where USERNAME = '%s';" %(username))
    baa = cursor.fetchall()
    na = []
    for b in baa:
        na.append(b)
    if len(na) != 0:
         return HttpResponse("<h1> This is working {} </h1>".format(na[0]))
    else:
        return HttpResponse("<h1> This is not working </h1>")
def mid(request, name):
        goo["name"] = name
        if request.method == "POST":

                term = request.POST.get('Term')
                sessi = request.POST.get("session")
                print(name)
                print(bo)
                print(sessi)
                print(term)
                bb = "CAT"
                ho = {}
                count = 0
                upp = sch.upper()
                print(upp)
                l = sessi.replace('/','_')
                koo3 = "Subjects"+l+""
                if name.upper() not in bo:
                     return HttpResponseRedirect("/studentapp/")
                else:
                    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= "SINCLAIR", autocommit = True)
                    cursor = db.cursor()
                    cursor.execute("select distinct SUBJECTS from {} where NAMES = '%s';".format(koo3) %( name ))
                    zee = cursor.fetchall()
                    print(zee)
                    for t in zee:
                        nn = []
                        count += 1
                        nn.append(count)
                        cursor.execute("select  CAT from RESULTS_CATS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
                        fer = cursor.fetchall()
                        print(fer)
                        if fer[0][0] == None:
                            nn.append("Not Available")
                        else:
                            nn.append(fer[0][0])
                        cursor.execute("select LOWEST, HIGHEST, GRADE, REMARKS from grade_table where CAT_EXAM = '%s';" %(bb))
                        ger = cursor.fetchall()
                        print(ger)
                        for p in ger:
                          if fer[0][0] in range(p[0],p[1]+1):
                            if p[2] == None:
                              nn.append("Not Available")
                            else:
                              nn.append(p[2])
                            if p[3] == None:
                               nn.append("Not Available")
                            else:

                                 nn.append(p[3])
                        cursor.execute("select CAT from RESULTS_CATS where SUBJECT = %s and TERM = %s and SESSION = %s;",( t[0], term, sessi))
                        dee = cursor.fetchall()
                        kl = 0
                        rl = 0
                        if len(dee) != 0:
                            for v in dee:
                                if v[0] != None:
                                    kl += v[0]
                                    rl += 1
                            coo = round(kl/rl, 2)
                            nn.append(coo)
                        else:
                            nn.append("Not Available")
                        print(nn)
                        ho[t[0]] = nn
                    cursor.execute("select AVERAGE from DOSSIER_CATS where SESSION = %s and TERM = %s and NAMES = %s;" , (sessi, term, name))
                    fal = cursor.fetchall()
                    if len(fal) != 0:
                            avg = fal[0][0]
                    cursor.execute("select COMMENTS_ADMIN from DOSSIER_CATS where  NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ver = cursor.fetchall()
                    if len(ver) != 0:
                            if ver[0][0] == None:
                                comms = "Not Available"
                            else:
                                comms = ver[0][0]
                    cursor.execute("select COMMENTS_TEACHER from DOSSIER_CATS where NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ber = cursor.fetchall()
                    if len(ber) != 0:
                        if ver[0][0] == None:
                                bomms = "Not Available"
                        else:
                                bomms = ver[0][0]
                        #if fal[0][0] == None:
                         #   nn.append("Not Available")
                        #else:
                         #   nn.append("Not Available")

                    return  render(request,'studentapp/mid1.html',{'pic':img, 'stud': name, "dat": ho, "avg":avg, "comms": comms, "bomms":bomms} )
        else:
            form = bars(request.POST)
        return  render(request,'studentapp/mid1.html',{'pic':img, 'stud': name} )
def CAT(request):
        name = goo["name"]
        print(goo)
        if name not in bo:
            return HttpResponseRedirect("/studentapp/")
        else:
            if request.method == "POST":

                term = request.POST.get('Term')
                sessi = request.POST.get("session")
                bb = "CAT"
                ho = {}
                count = 0
                upp = sch.upper()
                print(upp)
                l = sessi.replace('/','_')
                koo3 = "Subjects"+l+""
                if name.upper() not in bo:
                     return HttpResponseRedirect("/studentapp/")
                else:
                    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= "SINCLAIR", autocommit = True)
                    cursor = db.cursor()
                    cursor.execute("select distinct SUBJECTS from {} where NAMES = '%s';".format(koo3) %( name ))
                    zee = cursor.fetchall()
                    print(zee)
                    for t in zee:
                        nn = []
                        count += 1
                        nn.append(count)
                        cursor.execute("select  CAT from RESULTS_CATS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
                        fer = cursor.fetchall()
                        print(fer)
                        if fer[0][0] == None:
                            nn.append("Not Available")
                        else:
                            nn.append(fer[0][0])
                        cursor.execute("select LOWEST, HIGHEST, GRADE, REMARKS from grade_table where CAT_EXAM = '%s';" %(bb))
                        ger = cursor.fetchall()
                        print(ger)
                        for p in ger:
                          if fer[0][0] in range(p[0],p[1]+1):
                            if p[2] == None:
                              nn.append("Not Available")
                            else:
                              nn.append(p[2])
                            if p[3] == None:
                               nn.append("Not Available")
                            else:

                                 nn.append(p[3])
                        cursor.execute("select CAT from RESULTS_CATS where SUBJECT = %s and TERM = %s and SESSION = %s;",( t[0], term, sessi))
                        dee = cursor.fetchall()
                        kl = 0
                        rl = 0
                        if len(dee) != 0:
                            for v in dee:
                                if v[0] != None:
                                    kl += v[0]
                                    rl += 1
                            coo = round(kl/rl, 2)
                            nn.append(coo)
                        else:
                            nn.append("Not Available")
                        print(nn)
                        ho[t[0]] = nn
                    cursor.execute("select AVERAGE from DOSSIER_CATS where SESSION = %s and TERM = %s and NAMES = %s;" , (sessi, term, name))
                    fal = cursor.fetchall()
                    if len(fal) != 0:
                            avg = fal[0][0]
                    cursor.execute("select COMMENTS_ADMIN from DOSSIER_CATS where  NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ver = cursor.fetchall()
                    if len(ver) != 0:
                            if ver[0][0] == None:
                                comms = "Not Available"
                            else:
                                comms = ver[0][0]
                    cursor.execute("select COMMENTS_TEACHER from DOSSIER_CATS where NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ber = cursor.fetchall()
                    if len(ber) != 0:
                        if ver[0][0] == None:
                                bomms = "Not Available"
                        else:
                                bomms = ver[0][0]
                        #if fal[0][0] == None:
                         #   nn.append("Not Available")
                        #else:
                         #   nn.append("Not Available")

                    return  render(request,'studentapp/CAT.html',{'pic':img, 'stud': name, "dat": ho, "avg":avg, "comms": comms, "bomms":bomms} )
            else:
                     form = bars(request.POST)
        return  render(request,'studentapp/CAT.html',{'pic':img, 'stud': name} )
def Exam(request):
        name = goo["name"]
        if name not in bo:
            return HttpResponseRedirect("/studentapp/")
        else:
            if request.method == "POST":

                term = request.POST.get('Term')
                sessi = request.POST.get("session")
                print(goo)
                print(bo)
                print(sessi)
                print(term)
                bb = "Exams"
                ho = {}
                count = 0
                upp = sch.upper()
                print(upp)
                l = sessi.replace('/','_')
                koo3 = "Subjects"+l+""
                if name.upper() not in bo:
                     return HttpResponseRedirect("/studentapp/")
                else:
                    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= "SINCLAIR", autocommit = True)
                    cursor = db.cursor()
                    cursor.execute("select distinct SUBJECTS from {} where NAMES = '%s';".format(koo3) %( name ))
                    zee = cursor.fetchall()
                    print(zee)
                    for t in zee:
                        nn = []
                        count += 1
                        nn.append(count)
                        cursor.execute("select  CAT from RESULTS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
                        fer = cursor.fetchall()
                        print(fer)
                        if fer[0][0] == None:
                            nn.append("Not Available")
                        else:
                            nn.append(fer[0][0])
                        cursor.execute("select LOWEST, HIGHEST, GRADE, REMARKS from grade_table where CAT_EXAM = '%s';" %(bb))
                        ger = cursor.fetchall()
                        print(ger)
                        for p in ger:
                          if fer[0][0] in range(p[0],p[1]+1):
                            if p[2] == None:
                              nn.append("Not Available")
                            else:
                              nn.append(p[2])
                            if p[3] == None:
                               nn.append("Not Available")
                            else:

                                 nn.append(p[3])
                        cursor.execute("select CAT from RESULTS where SUBJECT = %s and TERM = %s and SESSION = %s;",( t[0], term, sessi))
                        dee = cursor.fetchall()
                        kl = 0
                        rl = 0
                        if len(dee) != 0:
                            for v in dee:
                                if v[0] != None:
                                    kl += v[0]
                                    rl += 1
                            coo = round(kl/rl, 2)
                            nn.append(coo)
                        else:
                            nn.append("Not Available")
                        print(nn)
                        ho[t[0]] = nn
                    cursor.execute("select AVERAGE from DOSSIER where SESSION = %s and TERM = %s and NAMES = %s;" , (sessi, term, name))
                    fal = cursor.fetchall()
                    if len(fal) != 0:
                            avg = fal[0][0]
                    cursor.execute("select COMMENTS_ADMIN from DOSSIER where  NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ver = cursor.fetchall()
                    if len(ver) != 0:
                            if ver[0][0] == None:
                                comms = "Not Available"
                            else:
                                comms = ver[0][0]
                    cursor.execute("select COMMENTS_TEACHER from DOSSIER where NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ber = cursor.fetchall()
                    if len(ber) != 0:
                        if ver[0][0] == None:
                                bomms = "Not Available"
                        else:
                                bomms = ver[0][0]
                        #if fal[0][0] == None:
                         #   nn.append("Not Available")
                        #else:
                         #   nn.append("Not Available")

                    return  render(request,'studentapp/Exam.html',{'pic':img, 'stud': name, "dat": ho, "avg":avg, "comms": comms, "bomms":bomms} )
            else:
                     form = bars(request.POST)
        return  render(request,'studentapp/Exam.html',{'pic':img, 'stud': name} )

def weekly(request):

        name = goo["name"]
        if name not in bo:
            return HttpResponseRedirect("/studentapp/")
        else:
            if request.method == "POST":

                term = request.POST.get('Term')
                sessi = request.POST.get("session")
                week = request.POST.get("weekly")
                print(goo)
                print(bo)
                print(sessi)
                print(term)
                bb = "Exams"
                ho = {}
                count = 0
                upp = sch.upper()
                print(upp)
                l = sessi.replace('/','_')
                koo3 = "Subjects"+l+""
                if name.upper() not in bo:
                     return HttpResponseRedirect("/studentapp/")
                else:
                    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= "SINCLAIR", autocommit = True)
                    cursor = db.cursor()
                    cursor.execute("select distinct SUBJECTS from {} where NAMES = '%s';".format(koo3) %( name ))
                    zee = cursor.fetchall()
                    print(zee)
                    for t in zee:
                        nn = []
                        count += 1
                        nn.append(count)
                        cursor.execute("select  CAT from RESULTS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
                        fer = cursor.fetchall()
                        print(fer)
                        if fer[0][0] == None:
                            nn.append("Not Available")
                        else:
                            nn.append(fer[0][0])
                        cursor.execute("select LOWEST, HIGHEST, GRADE, REMARKS from grade_table where CAT_EXAM = '%s';" %(bb))
                        ger = cursor.fetchall()
                        print(ger)
                        for p in ger:
                          if fer[0][0] in range(p[0],p[1]+1):
                            if p[2] == None:
                              nn.append("Not Available")
                            else:
                              nn.append(p[2])
                            if p[3] == None:
                               nn.append("Not Available")
                            else:

                                 nn.append(p[3])
                        cursor.execute("select CAT from RESULTS where SUBJECT = %s and TERM = %s and SESSION = %s;",( t[0], term, sessi))
                        dee = cursor.fetchall()
                        kl = 0
                        rl = 0
                        if len(dee) != 0:
                            for v in dee:
                                if v[0] != None:
                                    kl += v[0]
                                    rl += 1
                            coo = round(kl/rl, 2)
                            nn.append(coo)
                        else:
                            nn.append("Not Available")
                        print(nn)
                        ho[t[0]] = nn
                    cursor.execute("select AVERAGE from DOSSIER where SESSION = %s and TERM = %s and NAMES = %s;" , (sessi, term, name))
                    fal = cursor.fetchall()
                    if len(fal) != 0:
                            avg = fal[0][0]
                    cursor.execute("select COMMENTS_ADMIN from DOSSIER where  NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ver = cursor.fetchall()
                    if len(ver) != 0:
                            if ver[0][0] == None:
                                comms = "Not Available"
                            else:
                                comms = ver[0][0]
                    cursor.execute("select COMMENTS_TEACHER from DOSSIER where NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
                    ber = cursor.fetchall()
                    if len(ber) != 0:
                        if ver[0][0] == None:
                                bomms = "Not Available"
                        else:
                                bomms = ver[0][0]
                        #if fal[0][0] == None:
                         #   nn.append("Not Available")
                        #else:
                         #   nn.append("Not Available")

                    return  render(request,'studentapp/weekly.html',{'pic':img, 'stud': name, "dat": ho, "avg":avg, "comms": comms, "bomms":bomms} )
            else:
                     form = bars(request.POST)
        return  render(request,'studentapp/weekly.html',{'pic':img, 'stud': name} )
def bar(request):
    opt = bars(request.POST)
    if request.method == 'POST':
        opt = bars(request.POST)
        if opt.is_valid():
            sessi = request.POST.get('Term')
            term = request.POST.get("session")

            #print(sessi)
            #print(term)
def Logins(request):

    form = login(request.POST)
    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= 'root', autocommit = True)
    db.connect()
    if request.method == 'POST':
        form = login(request.POST)
        username = request.POST.get("users")
        passwor = request.POST.get("passes")
        sch = request.POST.get("school")
        status = request.POST.get("status")
        print(status)
        #print(sch)
        if form.is_valid():

            #form.add_error(None, 'Invalid Password or Username')
            info["school"] = sch.upper()
            request.session["school"] = sch.upper()
            db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= sch.upper(), autocommit = True)
            db.connect()
            cursor = db.cursor()
            vcx = 'root'
            sessi = sess.replace('/','_')
            stud = "class_student_"+sessi+""
            if status == "Class Teacher" :

             cursor.execute("USE %s;" %(vcx,))
             cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO, STATUS from schools_info where SCHOOL_USERNAME = '%s';" %(sch.upper()))
             go = cursor.fetchall()
             cursor.execute("USE %s;" %(sch.upper(),))
             if len(go) != 0:
               if go[0][4] != "LOCKED":

                  cursor.execute("select CHG_PASSWORD, CLASS, STATUS, TEACHER_NAME from pass_table where CHG_USERNAME = %s and POSITION = %s ;" ,(username, status))
                  bol = cursor.fetchall()
                  if len(bol) != 0:
                      if bol[0][2] != "LOCKED":

                         if bol[0][0] == passwor:
                             request.session["status"] = status
                             info["status"] = status
                             if bol[0][3] != None:
                                 nana = bol[0][3]
                             if bol[0][1] != None:
                                 request.session["class"] = bol[0][1]
                                 info["class"] = bol[0][1]
                                 bebe = bol[0][1]
                             if go[0][0] != None:
                                 ss = go[0][0]
                             else:
                                  ss = "Not Available"
                             if go[0][1] != None:
                                  aa = go[0][1]
                             else:
                                   aa = 'Not Available'
                             if go[0][2] != None:
                                  cc = go[0][2]
                             else:
                                 cc = 'Not Available'
                             if go[0][3] != None:
                                 image_sch = b64decode(go[0][3])
                                 km =  "studentapp/static/studentapp/sch.jpg"
                                 with open(km, 'wb') as koo:
                                      koo.write(image_sch)

                             cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(bol[0][1]))
                             fern = cursor.fetchall()


                             if len(fern) != 0:
                                 ye = {}

                                 for xx in range(len(fern)):
                                     nu = []
                                     nu.append(fern[xx][0])
                                     cursor.execute("select SEX from Student_DATA where STUDENT_NAME = '%s';" %(fern[xx][0]))
                                     poo = cursor.fetchall()
                                     if len(poo) != 0:
                                         nu.append(poo[0][0])
                                     else:
                                         nu.append("Unavailable")
                                     ye['{}'.format(xx+1)] = nu

                         return  render(request,'studentapp/WT.html', {"dat": ye, "sch":ss, "address":aa, "motto":cc, "class":bebe,"teach":nana})
            if status == "Subject Teacher":
                 cursor.execute("USE %s;" %(vcx,))
                 cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO, STATUS from schools_info where SCHOOL_USERNAME = '%s';" %(sch.upper()))
                 go = cursor.fetchall()
                 cursor.execute("USE %s;" %(sch.upper(),))
                 if len(go) != 0:
                      if go[0][4] != "LOCKED":

                            cursor.execute("select CHG_PASSWORD, CLASS, STATUS, TEACHER_NAME from pass_table where CHG_USERNAME = '%s';" %(username))
                            bol = cursor.fetchall()
                            if len(bol) != 0:
                                if bol[0][2] != "LOCKED":

                                    if bol[0][0] == passwor:
                                        request.session["status"] = status

                                        if bol[0][3] != None:
                                            nana = bol[0][3]
                                        if bol[0][1] != None:
                                            request.session["class"] = bol[0][1]
                                            bebe = bol[0][1]
                                        if go[0][0] != None:
                                             ss = go[0][0]
                                        else:
                                          ss = "Not Available"
                                        if go[0][1] != None:
                                            aa = go[0][1]
                                        else:
                                            aa = 'Not Available'
                                        if go[0][2] != None:
                                             cc = go[0][2]
                                        else:
                                            cc = 'Not Available'
                                        if go[0][3] != None:
                                             image_sch = b64decode(go[0][3])
                                             km =  "studentapp/static/studentapp/sch.jpg"
                                             with open(km, 'wb') as koo:
                                                koo.write(image_sch)
                                        if bol[0][3] != None:
                                             teca = bol[0][3]
                                             request.session["T_name"] = bol[0][3]
                                             cursor.execute("select SUBJECTS, CLASS from subject_teacher where TEACHER_NAME = '%s';" %(bol[0][3]))
                                             vee = cursor.fetchall()

                                             if len(vee) != 0:
                                                 bt = []
                                                 nt = []
                                                 for nn in vee:
                                                     bt.append(nn[0])
                                                     nt.append(nn[1])
                                                     #bt[nn[0]] = nn[1]

                                                 request.session["subjt"] = bt
                                                 request.session["claxt"] = nt
                                                 #bvv = request.session["sub_tea"]

                                                 return  render(request,'studentapp/sub_E.html', {"pic": img, "sch":ss, "address":aa,\
                                                                        "motto":cc, "teach": teca})


                                        else:
                                             return render(request, 'studentapp/index.html', {'form': form})

                                    else:
                                         return render(request, 'studentapp/index.html', {'form': form})


                                else:
                                       return render(request, 'studentapp/index.html', {'form': form})
                      else:
                          return render(request, 'studentapp/index.html', {'form': form})

            if status == "Parent":
             cursor.execute("select CHG_PASSWORD, STATUS, PARENT_NAME from parent_pass where CHG_USERNAME = %s and POSITION = %s;" ,(username, status))
             baa = cursor.fetchall()
             if len(baa) != 0:
               if baa[0][1] != "LOCKED":
                if baa[0][0] == passwor:
                    if baa[0][2] != None:
                        nana = baa[0][2]
                    parent = baa[0][0]
                    cursor.execute("USE %s;" %(vcx,))
                    cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO, STATUS from schools_info where SCHOOL_USERNAME = '%s';" %(sch.upper()))
                    go = cursor.fetchall()
                    info["status"] = status
                    if go[0][0] != None:
                        ss = go[0][0]
                    else:
                       ss = "Not Available"
                    if go[0][1] != None:
                        aa = go[0][1]
                    else:
                          aa = 'Not Available'
                    if go[0][2] != None:
                         cc = go[0][2]
                    else:
                        cc = 'Not Available'
                    if go[0][3] != None:
                         image_sch = b64decode(go[0][3])
                         km =  "studentapp/static/studentapp/sch.jpg"
                         with open(km, 'wb') as koo:
                           koo.write(image_sch)
                    cursor.execute("USE %s;" %(sch.upper(),))
                    cursor.execute("select STUDENT_NAME from web_table where USERNAME  = '%s';" %(username))
                    mo = cursor.fetchall()
                    if len(mo) != 0:


                         fer = {}



                         for w in mo:
                            if w[0].upper() not in bo:
                                  bo.append(w[0].upper())


                         for b in range(len(bo)):
                             cursor.execute("select * from Student_DATA where STUDENT_NAME = '%s';" %(bo[b]))
                             vo = cursor.fetchall()
                             if len(vo) != 0:
                                 for f in vo:
                                     ran = []
                                     if f[1] != None:
                                          ran.append(f[1])
                                     else:
                                        ran.append('Not Available')
                                     if f[2] != None:
                                        ran.append(f[2])
                                     else:
                                         ran.append('Not Available')
                                     if f[3] != None:
                                         ran.append(f[3])
                                     else:
                                          ran.append("Not Available")
                                     if f[4] != None:
                                        ran.append(f[4])
                                     else:
                                         ran.append("Not Available")
                                     if f[6] != None:
                                        ran.append(f[6])
                                     else:
                                         ran.append("Not Available")
                                     if f[7] != None:
                                         ran.append(f[7])
                                     else:
                                         ran.append("Not Available")
                                     if f[8] != None:
                                        ran.append(f[8])
                                     else:
                                         ran.append("Not Available")
                                     if f[9] != None:
                                         ran.append(f[9])
                                     else:
                                          ran.append("Not Available")
                                     if f[10] != None:
                                         #image_data = b64encode(f[10]).decode('ascii')
                                        image_data = b64decode(f[10])
                                        kk =  "studentapp/static/studentapp/{}.jpg".format(b)
                                        mm = "studentapp/{}.jpg".format(b)
                                        img[bo[b]] = mm

                                  #try:
                                      #os.makedirs(kk)
                                        with open(kk, 'wb') as koo:
                                            koo.write(image_data)
                                  #except OSError:
                                     # pass
                                  #image_data = binascii.b2a_base64(f[10])
                                  #image_data = struct.pack('I', f[10]).encode('base64')
                                  #img.append(image_data)
                                  #print(img)
                                 fer[bo[b]] = ran

                                  #pic = ContentFile(image_data, '{}.png'.format(b))
                                  #pic.save()

                    return  render(request,'studentapp/home.html', {"data": fer, "pic": img, "sch":ss, "address":aa,\
                                                                    "motto":cc, "teach": nana})
               else:
                   return render(request, 'studentapp/index.html', {'form': form})
             else:
                 return render(request, 'studentapp/index.html', {'form': form})
            #else:
                #raise form.ValidationError("wrong login details")
            #return render(request, 'studentapp/index.html', {'form': form})
            #return HttpResponse("<h1> you are looking at the question </h1>")
              #return render(request, 'studentapp/index_pass.html', {'form': form})

           # else:
    else:        #form = login()
         form = login()            #raise form.ValidationError( ("passwords not the same "))
    return render(request, 'studentapp/index.html', {'form': form})
        # HttpResponse("<h1> This is not working </h1>")

def Logins_pass(request):
    form = login_pass(request.POST)
    if request.method == 'POST':
        form = login_pass(request.POST)
        if not form.is_valid():

            #form.add_error(None, 'Invalid Password or Username')

            #return render(request, 'studentapp/index_pass.html', {'form': form})

            username = request.POST.get("users")
            passwor = request.POST.get("passes")
            sch = request.POST.get("school")
            new_pass = request.POST.get("new passes")
            con_pass = request.POST.get("con passes")

            db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                              host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= sch.upper(), autocommit = True)
            cursor = db.cursor()
            if new_pass == con_pass:
                cursor.execute("select CHG_PASSWORD from parent_pass where USERNAME = '%s';" %(username))
                baa = cursor.fetchall()
                if baa[0][0] == passwor:
                    loo = "Parent"
                    cursor.execute("UPDATE parent_pass SET CHG_PASSWORD = %s where CHG_USERNAME = %s and \
                                                 CHG_PASSWORD = %s and  POSITION = %s ;", (con_pass, username, passwor,loo))
                    return HttpResponse("<h1> sucessfully change password</h1>")
            else:
                return render(request, "studentapp/index_pass.html",{'form': form} )

    else:
        form = login_pass()
    return render(request, 'studentapp/index22.html', {'form': form})

def men (request):
    form = login_pass(request.POST)
    if request.method == 'POST':
        form = login(request.POST)
        #if not form.is_valid():

    return render(request, 'studentapp/try.html', {'form': form})

def Logins_user(request):
    form = login_user(request.POST)
    if request.method == 'POST':
        form = login(request.POST)
        if not form.is_valid():
            raise form.ValidationError( ("passwords not the same "))
            print(form.errors)
            #form.add_error(None, 'Invalid Password or Username')
            print("Nooooo")
            return render(request, 'studentapp/index_user.html', {'form': form})
        else:
            username = form.cleaned_data.get("users")
            password = form.cleaned_data.get("passes")
            sch = form.cleaned_data.get("school")
            new_user = form.cleaned_data.get("new user")
            con_user = form.cleaned_data.get("con user")
            print("{} {} {}".format(username,password, sch, con_user, new_user))
            db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                              host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= sch.upper(), autocommit = True)
            if new_user == con_user:
                cursor = db.cursor()
                cursor.execute("select CHG_PASSWORD from parent_pass where USERNAME = '%s';" %(username))
                baa = cursor.fetchall()
                if baa[0][0] == password:
                    cursor.execute("select CHG_USERNAME from parent_pass;")
                    voo = cursor.fetchall()
                    mot = []
                    for i in voo:
                        mot.append(i[0])
                    if con_user not in mot:
                        return HttpResponseRedirect("/aaah")
                    else:
                        raise form.ValidationError( ("Username exists "))
                else:
                    raise form.ValidationError( ("wrong login details"))
            else:
                raise form.ValidationError( ("Username not the same "))
    else:
        form = login()
        return render(request, 'studentapp/index_user.html', {'form': form})


def teacher_CAT(request):


      schl = request.session["school"]
      db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                     host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
      db.connect()
      cursor = db.cursor()
      vcx = 'root'
      sessi = sess.replace('/','_')
      stud = "class_student_"+sessi+""
      sub = "Subjects"+sessi+""
      cursor.execute("USE %s;" %(vcx,))
      cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
      go = cursor.fetchall()

      if go[0][0] != None:
          ss = go[0][0]
      else:
            ss = "Not Available"
      if go[0][1] != None:
              aa = go[0][1]
      else:
            aa = 'Not Available'
      if go[0][2] != None:
           cc = go[0][2]
      else:
            cc = 'Not Available'
      if go[0][3] != None:
                 image_sch = b64decode(go[0][3])
                 km =  "studentapp/static/studentapp/sch.jpg"
                 with open(km, 'wb') as koo:
                    koo.write(image_sch)
      if request.method == "POST":
            name = request.POST.get('student')
            cat = request.POST.get('CAT')
            catz = cat.replace(' ','_')
            term = request.POST.get("Term")

            cursor.execute("USE %s;" %(schl,))
            #cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(info["class"]))
            #poo = cursor.fetchall()
            #if len(poo) != 0:
            #    nu = []
            #    tu = {}
            #    for dd in poo:
            #        nu.append(dd[0])
            #    tu["Names"] = nu
            #if request.method == "POST":
            name = request.POST.get('student')
            cat = request.POST.get('CAT')
            catz = cat.replace(' ','_')
            term = request.POST.get("Term")
            cursor.execute("select SUBJECTS from {} where CLASS = %s and NAMES = %s;".format(sub), (clazz, name))
            lor = cursor.fetchall()
            print(lor)
            cursor.execute("select distinct SUBJECTS, {} from CATS_EXAMS where SESSION = %s and TERM = %s and CLASS = %s and NAMES = %s;".format(catz), (sess,term,info["class"],name))
            ff = cursor.fetchall()
            mu = []
            if len(lor) != 0:
                    der = {}
                    for g in lor:
                       mu.append(g[0])
                    if len(ff) != 0:
                        for h in ff:
                           if h[1] != None:
                               if h[0] in mu:
                                 mu.remove(h[0])
                    der["subjects"] = mu
                    print("okay")
                    print(der)
                    return  render(request,'studentapp/TCAT.html',{'subjects':der, 'name': name, "sch":ss, "address":aa, "motto":cc, "CAT":cat, "Term": term} )
            #else:
             #       return  render(request,'studentapp/TCAT.html',{'student': tu, "sch":ss, "address":aa, "motto":cc} )
            #if request.POST.get("sends"):
             #     print("sends")
              #    cat = request.POST.get('CAT')
               #   catz = cat.replace(' ','_')
                #  for d in mu:
                 #     xx = request.POST.get("{}".format(d))
                  #    cursor.execute("insert CATS_EXAMS ({}, SESSION, NAMES, CLASS, TERM, SUBJECTS) values (%s, %s, %s, %s, %s, %s);".format(catz), (xx,sess,name,info["class"], term, d))
                  #cursor.execute("select {}, SUBJECTS from CATS_EXAMS where NAMES = %s and CLASS = %s and SESSION = %s and TERM = %s;".format(catz), (name, info["class"],sess, term))
             #     dor = cursor.fetchall()
              #    print(dor)
               #   if len(dor) != 0:
                #      for tt in dor:
                 #         vu = []
                  #        cu = {}
                   #       cu[tt[1]] = tt[0]
                          #cu.append(tt[1])
                          #cu.append(tt[0])
                      #bur = {}
                      #bur["score"] = vu
                      #ber = {}
                      #ber["subjects"] = cu
                      #return  render(request,'studentapp/TShow.html',{'subjects':der, 'score': vu, "sch":ss, "address":aa, "motto":cc, "name": name, "pat": cat} )
      else:
                    return  render(request,'studentapp/TCAT.html',{ "sch":ss, "address":aa, "motto":cc} )

def subj_page(request):
    schl = request.session["school"]

    if request.method == "POST":

        ses = request.POST.get("session")
        term = request.POST.get("Term")
        cat = request.POST.get('CAT')
        subj = request.POST.get('subj')
        clazz = request.POST.get('clax')

        db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
        db.connect()
        ret = request.session["claxt"]
        rek = request.session["subjt"]
        joo = {}
        for rr in range(len(ret)):
             if ret[rr] == clazz:
                 if rek[rr] == subj:
                     joo[subj] = clazz
        #request.session["subjects"] = mu
                     request.session["class"] = clazz
                     request.session["term"] = term
                     request.session["CAT"]  = cat
                     request.session["subs"] = joo
                     return HttpResponseRedirect("subject/")
    else:
      if request.method == "GET":
        nuu = request.session["subjt"]
        cuu = request.session["claxt"]

        db = mysql.connector.connect(user = 'gbiggsDB', password='passworded',
                                          host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
        db.connect()
        cursor = db.cursor()
        vcx = 'root'
        sessi = sess.replace('/','_')
        stud = "class_student_"+sessi+""
        sub = "Subjects"+sessi+""
        cursor.execute("USE %s;" %(vcx,))
        cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
        go = cursor.fetchall()
        if go[0][0] != None:
            ss = go[0][0]
        else:
            ss = "Not Available"
        if go[0][1] != None:
              aa = go[0][1]
        else:
             aa = 'Not Available'
        if go[0][2] != None:
            cc = go[0][2]
        else:
             cc = 'Not Available'
        if go[0][3] != None:
                image_sch = b64decode(go[0][3])
                km =  "studentapp/static/studentapp/sch.jpg"
                with open(km, 'wb') as koo:
                     koo.write(image_sch)

        return  render(request,'studentapp/suby.html', {"subj":nuu,"clas":cuu, "pic": img, "sch":ss, "address":aa,"motto":cc })


def subby(request):

    schl = request.session["school"]
    if request.method == "GET":

        db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
        db.connect()
        cursor = db.cursor()
        vcx = 'root'
        sessi = sess.replace('/','_')
        stud = "class_student_"+sessi+""
        sub = "Subjects"+sessi+""
        cursor.execute("USE %s;" %(vcx,))
        cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
        go = cursor.fetchall()
        if go[0][0] != None:
          ss = go[0][0]
        else:
            ss = "Not Available"
        if go[0][1] != None:
              aa = go[0][1]
        else:
             aa = 'Not Available'
        if go[0][2] != None:
            cc = go[0][2]
        else:
             cc = 'Not Available'
        if go[0][3] != None:
            image_sch = b64decode(go[0][3])
            km =  "studentapp/static/studentapp/sch.jpg"
            with open(km, 'wb') as koo:
                 koo.write(image_sch)
        moo = request.session["subs"]
        cat = request.session["CAT"]
        catz = cat.replace(' ','_')
        term = request.session["term"]
        cursor.execute("USE %s;" %(schl,))

        if len(moo) == 1:
            for m in moo:
             suj = m
             xxl = moo[m]

             cursor.execute("select NAMES from {} where CLASS = %s and SUBJECTS = %s;".format(sub), (xxl, suj))
             lor = cursor.fetchall()
             print(lor)
             cursor.execute("select distinct NAMES, {} from CATS_EXAMS where SESSION = %s and TERM = %s and CLASS = %s and SUBJECTS = %s;".format(catz), (sess,term,xxl,suj))
             ff = cursor.fetchall()
             mu = []
             if len(lor) != 0:
                der = {}
                for g in lor:
                   mu.append(g[0])
                if len(ff) != 0:
                    for h in ff:
                        if h[1] != None:
                            if h[0] in mu:
                                mu.remove(h[0])
                                print(mu)

             request.session["subjects"] = mu
             vee = request.session["subjects"]
             print(vee)
        return  render(request,'studentapp/TCAT.html', {"subjects": vee,"CAT":cat, "sch":ss, "address":aa, "motto":cc, "class":xxl,\
                                                      "name":suj,"Term":term})
    else:
        if request.method == "POST":
            schl = request.session["school"]
            db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                     host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
            db.connect()
            cursor = db.cursor()
            vcx = 'root'
            sessi = sess.replace('/','_')
            stud = "class_student_"+sessi+""
            sub = "Subjects"+sessi+""
            #request.session["class"] = clazz
            term = request.session["term"]
            cat = request.session["CAT"]
            moo = request.session["subs"]
            cat = request.POST.get('CAT')
            catz = cat.replace(' ','_')
            if len(moo) == 1:
                for m in moo:
                     suj = m
                     xxl = moo[m]

            cursor.execute("USE %s;" %(schl,))
            #cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(info["class"]))
            #poo = cursor.fetchall()
            #if len(poo) != 0:

            cursor.execute("select distinct NAMES, {} from CATS_EXAMS where SESSION = %s and TERM = %s and CLASS = %s and SUBJECTS = %s;".format(catz), (sess,term,xxl,suj))
            ff = cursor.fetchall()
            mu = []
            bu = []
            subj = request.session["subjects"]


            coo = 0
            if len(moo) == 1:
                 for m in moo:
                     suj = m
                     xxl = moo[m]

            for d in subj:
                     xx = request.POST.get("{}".format(d))

                     if xx.isdigit():

                         cursor.execute("select {} from CATS_EXAMS where SUBJECTS = %s and CLASS = %s and SESSION = %s and TERM = %s and NAMES = %s;".format(catz), (suj, xxl,sess, term, d))
                         dor = cursor.fetchall()

                         if len(dor) == 0:
                                 cursor.execute("INSERT INTO CATS_EXAMS ({}, SESSION, NAMES, CLASS, TERM, SUBJECTS) values (%s, %s, %s, %s, %s, %s);".format(catz),\
                                                (xx,sess,d,xxl, term, suj))

            return HttpResponseRedirect("http://127.0.0.1:8000/studentapp/teacher/subj/")
def comms_btn(request):

    schl = request.session["school"]
    stud = "class_student_"+sess+""
    if request.method =="GET":
        db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
        db.connect()
        cursor = db.cursor()
        vcx = 'root'
        sessi = sess.replace('/','_')
        stud = "class_student_"+sessi+""
        sub = "Subjects"+sessi+""
        cursor.execute("USE %s;" %(vcx,))
        cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
        go = cursor.fetchall()
        if go[0][0] != None:
          ss = go[0][0]
        else:
            ss = "Not Available"
        if go[0][1] != None:
              aa = go[0][1]
        else:
             aa = 'Not Available'
        if go[0][2] != None:
            cc = go[0][2]
        else:
             cc = 'Not Available'
        if go[0][3] != None:
            image_sch = b64decode(go[0][3])
            km =  "studentapp/static/studentapp/sch.jpg"
            with open(km, 'wb') as koo:
                 koo.write(image_sch)
        moo = request.session["subs"]
        cat = request.session["CAT"]
        catz = cat.replace(' ','_')
        term = request.session["term"]
        clax = request.session["class"]
        cursor.execute("USE %s;" %(schl,))
        cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(clax))
        fern = cursor.fetchall()
        if len(fern) != 0:
            fu = []
            for c in fern:
                fu.append(c[0])
            request.session["names"] = fu
            kom ={}
            kom["student"] = fu
        return  render(request,'studentapp/T_CATT.html', {"dat": kom, "sch":ss, "address":aa, "motto":cc, "class":clax})
        #cursor.execute("select  CAT from RESULTS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
        #fer = cursor.fetchall()
    else:
        if request.method =="POST":
            name = request.POST.get("student")
            cat = request.POST.get("CAT")
            catz = cat.replace(' ','_')
            term = request.POST.get("Term")
            request.session["student"] = name
            request.session["CAT"] = cat
            request.session["term"] = term

            return HttpResponseRedirect("scores/")

def comment(request):
    schl = request.session["school"]
    stud = "class_student_"+sess+""
    term = request.POST.get("Term")
    name = request.session["student"]
    cat = request.session["CAT"]
    term = request.session["term"]
    if request.method == "GET":
        db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
        db.connect()
        cursor = db.cursor()
        vcx = 'root'
        sessi = sess.replace('/','_')
        stud = "class_student_"+sessi+""
        sub = "Subjects"+sessi+""
        cursor.execute("USE %s;" %(vcx,))
        cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
        go = cursor.fetchall()
        if go[0][0] != None:
          ss = go[0][0]
        else:
            ss = "Not Available"
        if go[0][1] != None:
              aa = go[0][1]
        else:
             aa = 'Not Available'
        if go[0][2] != None:
            cc = go[0][2]
        else:
             cc = 'Not Available'
        if go[0][3] != None:
            image_sch = b64decode(go[0][3])
            km =  "studentapp/static/studentapp/sch.jpg"
            with open(km, 'wb') as koo:
                 koo.write(image_sch)
        ho = {}
        count = 0
        cursor.execute("select  CAT from RESULTS_CATS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
        zee = cursor.fetchall()
        print(zee)
        for t in zee:
                        nn = []
                        count += 1
                        nn.append(count)
                        cursor.execute("select  CAT from RESULTS_CATS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
                        fer = cursor.fetchall()
                        print(fer)
                        if fer[0][0] == None:
                            nn.append("Not Available")
                        else:
                            nn.append(fer[0][0])
                        cursor.execute("select LOWEST, HIGHEST, GRADE, REMARKS from grade_table where CAT_EXAM = '%s';" %(bb))
                        ger = cursor.fetchall()
                        print(ger)
                        for p in ger:
                          if fer[0][0] in range(p[0],p[1]+1):
                            if p[2] == None:
                              nn.append("Not Available")
                            else:
                              nn.append(p[2])
                            if p[3] == None:
                               nn.append("Not Available")
                            else:

                                 nn.append(p[3])
                        cursor.execute("select CAT from RESULTS_CATS where SUBJECT = %s and TERM = %s and SESSION = %s;",( t[0], term, sessi))
                        dee = cursor.fetchall()
                        kl = 0
                        rl = 0
                        if len(dee) != 0:
                            for v in dee:
                                if v[0] != None:
                                    kl += v[0]
                                    rl += 1
                            coo = round(kl/rl, 2)
                            nn.append(coo)
                        else:
                            nn.append("Not Available")
                        print(nn)
                        ho[t[0]] = nn
        cursor.execute("select AVERAGE from DOSSIER_CATS where SESSION = %s and TERM = %s and NAMES = %s;" , (sessi, term, name))
        fal = cursor.fetchall()
        if len(fal) != 0:
                avg = fal[0][0]
        cursor.execute("select COMMENTS_ADMIN from DOSSIER_CATS where  NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
        ver = cursor.fetchall()
        if len(ver) != 0:
              if ver[0][0] == None:
                     comms = "Not Available"
              else:
                     comms = ver[0][0]
        cursor.execute("select COMMENTS_TEACHER from DOSSIER_CATS where NAMES = %s and SESSION =%s and TERM = %s;", ( name,sessi,term))
        ber = cursor.fetchall()
        if len(ber) != 0:
            if ver[0][0] == None:
                    bomms = "Not Available"
            else:
                    bomms = ver[0][0]

        return  render(request,'studentapp/comment.html',{'pic':img, 'stud': name, "dat": ho, "avg":avg, "comms": comms, "bomms":bomms} )
        #cursor.execute("select ")
    else:
        if request.method == "GET":
            jj

def TCATT(request):

    schl = request.session["school"]
    stud = "class_student_"+sess+""
    if request.method =="GET":
        db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
        db.connect()
        cursor = db.cursor()
        vcx = 'root'
        sessi = sess.replace('/','_')
        stud = "class_student_"+sessi+""
        sub = "Subjects"+sessi+""
        cursor.execute("USE %s;" %(vcx,))
        cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
        go = cursor.fetchall()
        if go[0][0] != None:
          ss = go[0][0]
        else:
            ss = "Not Available"
        if go[0][1] != None:
              aa = go[0][1]
        else:
             aa = 'Not Available'
        if go[0][2] != None:
            cc = go[0][2]
        else:
             cc = 'Not Available'
        if go[0][3] != None:
            image_sch = b64decode(go[0][3])
            km =  "studentapp/static/studentapp/sch.jpg"
            with open(km, 'wb') as koo:
                 koo.write(image_sch)
        moo = request.session["subs"]
        cat = request.session["CAT"]
        catz = cat.replace(' ','_')
        term = request.session["term"]
        clax = request.session["class"]
        cursor.execute("USE %s;" %(schl,))
        cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(clax))
        fern = cursor.fetchall()
        if len(fern) != 0:
            fu = []
            for c in fern:
                fu.append(c[0])
            request.session["names"] = fu
        return  render(request,'studentapp/T_CATT.html', {"nam": fu, "sch":ss, "address":aa, "motto":cc, "class":clax})
        #cursor.execute("select  CAT from RESULTS where SUBJECT = %s and NAMES = %s and TERM = %s and SESSION = %s;", (t[0], name,term,sessi))
        #fer = cursor.fetchall()
    else:
        if request.method =="POST":
            db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
            db.connect()
            cursor = db.cursor()
            vcx = 'root'
            sessi = sess.replace('/','_')
            stud = "class_student_"+sessi+""
            sub = "Subjects"+sessi+""
            cursor.execute("USE %s;" %(vcx,))
            cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
            go = cursor.fetchall()
            if go[0][0] != None:
                ss = go[0][0]
            else:
                ss = "Not Available"
            if go[0][1] != None:
                  aa = go[0][1]
            else:
                 aa = 'Not Available'
            if go[0][2] != None:
                cc = go[0][2]
            else:
                 cc = 'Not Available'
            if go[0][3] != None:
                image_sch = b64decode(go[0][3])
                km =  "studentapp/static/studentapp/sch.jpg"
                with open(km, 'wb') as koo:
                     koo.write(image_sch)
            cursor.execute("USE %s;" %(schl,))
            clax = request.session["class"]
            cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(clax))
            fern = cursor.fetchall()
            if len(fern) != 0:
               fu = []
               for c in fern:
                   fu.append(c[0])
            request.session["names"] = fu
            moo = request.session["subs"]
            cat = request.POST.get("CAT")
            catz = cat.replace(' ','_')
            term = request.POST.get("Term")

            name = request.POST.get("stud_N")
            cursor.execute("select {}, SUBJECTS from CATS_EXAMS where NAMES = %s and SESSION = %s and TERM = %s and CLASS = %s;".format(catz), (name,sess,term, clax))
            cor = cursor.fetchall()
            print(cor)
            vz = {}
            cz = []
            if len(cor) != 0:

                for y in cor:
                    vz[y[1]] = y[0]

            return  render(request,'studentapp/T_CATT.html', {"nam": fu, "sch":ss, "address":aa, "motto":cc, "class":clax, "scores":vz, "cats":cat})



def second_page(request):

    schl = request.session["school"]
    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
    db.connect()
    cursor = db.cursor()
    vcx = 'root'
    sessi = sess.replace('/','_')
    stud = "class_student_"+sessi+""
    sub = "Subjects"+sessi+""
    cursor.execute("USE %s;" %(vcx,))
    cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
    go = cursor.fetchall()
    if go[0][0] != None:
      ss = go[0][0]
    else:
        ss = "Not Available"
    if go[0][1] != None:
          aa = go[0][1]
    else:
         aa = 'Not Available'
    if go[0][2] != None:
        cc = go[0][2]
    else:
         cc = 'Not Available'
    if go[0][3] != None:
            image_sch = b64decode(go[0][3])
            km =  "studentapp/static/studentapp/sch.jpg"
            with open(km, 'wb') as koo:
                 koo.write(image_sch)
    if request.method == "GET":


      stud = "class_student_"+sessi+""
      cursor.execute("USE %s;" %(schl,))
      clazz = request.session["class"]
      cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(clazz))
      fern = cursor.fetchall()
      if len(fern) != 0:
          tun = {}
          koo = []
          for v in fern:
              koo.append(v[0])
          tun["studd"] = koo
      return  render(request,'studentapp/teacher.html', {"dat": tun, "sch":ss, "address":aa, "motto":cc, "class":info["class"]})

    else:
        if request.method == "POST":
            name = request.POST.get('student')

            cat = request.POST.get('CAT')

            catz = cat.replace(' ','_')
            term = request.POST.get("Term")

           # db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                     #host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
            #db.connect()
            cursor = db.cursor()
            vcx = 'root'
            sessi = sess.replace('/','_')
            stud = "class_student_"+sessi+""
            sub = "Subjects"+sessi+""
            clazz = request.session["class"]
            cursor.execute("USE %s;" %(schl,))
            #cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(info["class"]))
            #poo = cursor.fetchall()
            #if len(poo) != 0:
            #    nu = []
            #    tu = {}
            #    for dd in poo:
            #        nu.append(dd[0])
            #    tu["Names"] = nu
            #if request.method == "POST":

            cursor.execute("select SUBJECTS from {} where CLASS = %s and NAMES = %s;".format(sub), (clazz, name))
            lor = cursor.fetchall()

            cursor.execute("select distinct SUBJECTS, {} from CATS_EXAMS where SESSION = %s and TERM = %s and CLASS = %s and NAMES = %s;".format(catz), (sess,term,clazz,name))
            ff = cursor.fetchall()

            mu = []
            if len(lor) != 0:
                    der = {}
                    for g in lor:
                       mu.append(g[0])
                    if len(ff) != 0:
                        for h in ff:
                           if h[1] != None:
                               if h[0] in mu:
                                 mu.remove(h[0])
                    request.session["subjects"] = mu
                    request.session["names"] = name
                    request.session["term"] = term
                    request.session["CAT"]  = catz
                    return HttpResponseRedirect("scores/")
                   # return  render(request,'studentapp/TCAT.html',{'subjects':der, 'name': name, "sch":ss, "address":aa, "motto":cc, "CAT":cat, "Term": term} )





def third_page(request):
    schl = request.session["school"]
    db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                 host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
    db.connect()
    cursor = db.cursor()
    vcx = 'root'
    sessi = sess.replace('/','_')
    stud = "class_student_"+sessi+""
    sub = "Subjects"+sessi+""
    cursor.execute("USE %s;" %(vcx,))
    cursor.execute("select SCHOOL_NAME, SCHOOL_ADDR, SCH_MOTTO, SCH_LOGO  from schools_info where SCHOOL_USERNAME = '%s';" %(schl))
    go = cursor.fetchall()
    if go[0][0] != None:
      ss = go[0][0]
    else:
        ss = "Not Available"
    if go[0][1] != None:
          aa = go[0][1]
    else:
         aa = 'Not Available'
    if go[0][2] != None:
        cc = go[0][2]
    else:
         cc = 'Not Available'
    if go[0][3] != None:
            image_sch = b64decode(go[0][3])
            km =  "studentapp/static/studentapp/sch.jpg"
            with open(km, 'wb') as koo:
                 koo.write(image_sch)
    if request.method == "GET":

      clasx = request.session["class"]
      stud = "class_student_"+sessi+""
      cursor.execute("USE %s;" %(schl,))
      cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(clasx))
      fern = cursor.fetchall()
      if len(fern) != 0:
          tun = {}
          koo = []
          for v in fern:
              koo.append(v[0])
          tun["studd"] = koo
          subj = request.session["subjects"]


          catz = request.session["CAT"]
          catzz = catz.replace("_"," ")
          term = request.session["term"]

          name = request.session["names"]
          claz = request.session["class"]
          return  render(request,'studentapp/TCAT.html', {"subjects": subj,"CAT":catzz, "sch":ss, "address":aa, "motto":cc, "class":claz,\
                                                      "name":name,"Term":term })


    else:

        if request.method == "POST":

            name = request.session['names']
            term = request.session["term"]
            #name = forr["names"]

            cat = request.session['CAT']
            #cat = forr['CAT']

            #print(cat)
            clazz = request.session["class"]
            catz = cat.replace(' ','_')

            #term = request.POST.get("Term")


            schl = request.session["school"]
            db = mysql.connector.connect(user= 'gbiggsDB', password='passworded',
                                     host='gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',database= schl, autocommit = True)
            db.connect()
            cursor = db.cursor()
            vcx = 'root'
            sessi = sess.replace('/','_')
            stud = "class_student_"+sessi+""
            sub = "Subjects"+sessi+""

            cursor.execute("USE %s;" %(schl,))
            #cursor.execute("select NAME from {} where CLASS = '%s';".format(stud) %(info["class"]))
            #poo = cursor.fetchall()
            #if len(poo) != 0:

            cursor.execute("select distinct SUBJECTS, {} from CATS_EXAMS where SESSION = %s and TERM = %s and CLASS = %s and NAMES = %s;".format(catz), (sess,term,clazz,name))
            ff = cursor.fetchall()
            mu = []
            bu = []
            subj = request.session["subjects"]
            clazz = request.session["class"]
            coo = 0

            for d in subj:
                     xx = request.POST.get("{}".format(d))

                     if xx.isdigit():

                         cursor.execute("select {} from CATS_EXAMS where NAMES = %s and CLASS = %s and SESSION = %s and TERM = %s and SUBJECTS = %s;".format(catz), (name, clazz,sess, term, d))
                         dor = cursor.fetchall()

                         if len(dor) == 0:
                                 cursor.execute("INSERT INTO CATS_EXAMS ({}, SESSION, NAMES, CLASS, TERM, SUBJECTS) values (%s, %s, %s, %s, %s, %s);".format(catz),\
                                                (xx,sess,name,clazz, term, d))

            return HttpResponseRedirect("http://127.0.0.1:8000/studentapp/teacher/CAT/")

            #    nu = []
            #    tu = {}
            #    for dd in poo:
            #        nu.append(dd[0])
            #    tu["Names"] = nu
            #if request.method == "POST":

            #cursor.execute("select SUBJECTS from {} where CLASS = %s and NAMES = %s;".format(sub), (info["class"], name))
           # lor = cursor.fetchall()
            #print(lor)
            #cursor.execute("select distinct SUBJECTS, {} from CATS_EXAMS where SESSION = %s and TERM = %s and CLASS = %s and NAMES = %s;".format(catz), (sess,term,info["class"],name))
            #ff = cursor.fetchall()
            #mu = []
            #if len(lor) != 0:
            #        der = {}
            #        for g in lor:
            #           mu.append(g[0])
            #        if len(ff) != 0:
            #            for h in ff:
            #               if h[1] != None:
            #                  if h[0] in mu:
            #                    mu.remove(h[0])
            #        der["subjects"] = mu
            #       print("okay")
            #       print(der)
            #        return  render(request,'studentapp/TCAT.html',{'subjects':der, 'name': name, "sch":ss, "address":aa, "motto":cc, "CAT":cat, "Term": term} )



def signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            print (form.errors)
            return render(request, 'studentapp/signup.html', {'form': form})
        else:
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            #new_user = User.objects.create_user(email=email,
              #                                  password=password,
                #                                     )
            #new_user.is_active = True
            #new_user.save()
            #return redirect('login')
    #else:
        #template = loader.get_template('studentapp/index.html')
         #form = SignUpForm()
      #  pass
    return render(request, 'studentapp/signup.html', {'form': form})
    #return HttpResponse("<h1> This is not working </h1>")

# Create your views here.

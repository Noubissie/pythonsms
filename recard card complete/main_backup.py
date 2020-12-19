import json
import os
import pandas as pd
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask import render_template, request, session, url_for, redirect, flash
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
#from flaskwebgui import FlaskUI
from database_head import app, db
from database import Database_Registration, CREUD, school_information,  staff_information, student_information, \
    subject_and_mark, exam_sequence, save_student_total_mark, annual_performance
# import flask_whooshalchemy as wa
# print('-->if port and local host are left black \nhost:local host\nport:8080')
# host = input('-->enter the host ip address or url::')
# port = input('-->enter the port number::')
#
# if host == '':
#     host = 'localhost'
#     port = '8080'



# UI = FlaskUI(app, host=host,port=port)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.secret_key = b'landry'


# @app.after_request  # after a request the response is not store in cache
# def after_request(response):
#     response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate, public,max-age=0"
#     response.headers['Expires'] = 0
#     response.headers['Pragma'] = "no-cache"
#     return response



@app.context_processor
def parse_json():
    return dict(jsonl=json.loads)

@app.route('/ADMIN/GBHS', methods=["GET"])
def admin():
    return render_template("administrator.html")

@app.context_processor
def length():
    return dict(length=len)

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/about_us')
def about_us():
    try:
        school_infolog = school_information.get_school_information_from_database()
        # staff_infolog = staff_information.get_staff_information()
        staff_infolog = Database_Registration.get_every_registrated_staff()
        student_infolog = student_information.get_student_information_from_database()
        return render_template('about_us.html', n=school_infolog, staff_infolog=staff_infolog,
                               student_infolog=student_infolog)
    except:
        return render_template('error page.html', about_us='block')


def number_of_evaluation():
    try:
        exams1 = exam_sequence(sequence=1)
        exams2 = exam_sequence(sequence=2)
        exams1st = exam_sequence(sequence='First term|Premiere tremestre')

        exams3 = exam_sequence(sequence=3)
        exams4 = exam_sequence(sequence=4)
        exams2rd = exam_sequence(sequence='Second Term|Deuxieme tremestre')

        exams5 = exam_sequence(sequence=5)
        exams6 = exam_sequence(sequence=6)
        exams3rd = exam_sequence(sequence='Third term|Troisieme tremestre')
        # annual = exam_sequence(sequence='Annual|Annuels')
        CREUD.save_to_database(exams1)
        CREUD.save_to_database(exams2)
        CREUD.save_to_database(exams1st)
        CREUD.save_to_database(exams3)
        CREUD.save_to_database(exams4)
        CREUD.save_to_database(exams2rd)
        CREUD.save_to_database(exams5)
        CREUD.save_to_database(exams6)
        CREUD.save_to_database(exams3rd)
    except:
        return render_template('error page.html', evaluation_has_not_been_inputed='block')
    # CREUD.save_to_database(annual)



@app.route('/registration')
def registration():
    try:
        school_info = school_information.get_school_information_from_database()

        return render_template('registration.html', school_info=school_info)
    except:
        return render_template('error page.html', registration_error='block')


@app.route('/administration_database', methods=["POST"])
def admin_database():
    number_of_class = request.form['number_of_class']
    number_of_staffs = request.form['number_of_staffs']
    sequence_creation = request.form['sequence_creation']
    if sequence_creation == 'ok':
        number_of_evaluation()

    if number_of_class != '':
        duplicated_classes = []
        school_section = request.form['school_section']
        school_year = request.form['school_year']


        for i in range(1, int(number_of_class) + 1):
            list_subjecto = []
            classes = request.form['class%s' % i]
            subjects_thought = request.form['subjects_thought%s' % i]
            file = request.files['class%i_file_subject' % i]
            if classes != '' and request.form['subjects_thought%s' % i] != '' and file.filename == '':

                class_subjects = subjects_thought.split(',')
                for j in class_subjects:
                    list_subjecto.append(j.replace('\r\n', ''))

                # json.dumps changes the list or other type to string
                # json.loads changes from string back to initial style

                list_subject = json.dumps(list_subjecto)

                try:
                    sch_info = school_information(school_section=school_section, school_year=school_year,
                                                  classs=classes,
                                                  subject_thought=list_subject)
                    CREUD.save_to_database(sch_info)
                except IntegrityError:
                    db.session.rollback()
                    duplicated_classes.append(classes)


                # list_class.append(classes)
            # return 'classes::%s  subjects%s'%(list_class,list_subject)

            elif request.form['subjects_thought%s' % i] == '' and request.files[
                'class%s_file_subject' % i].filename != '':
                file_subject_of_class_i = request.files['class%s_file_subject' % i]
                for i in file_subject_of_class_i.readlines():
                    list_subjecto.append(str(i, 'utf-8').replace('\r\n', ''))

                # app.config['UPLOAD_FOLDER'] = 'upload_subjects'
                # file_subject_of_class_i.save( os.path.join(app.config['UPLOAD_FOLDER'], file_subject_of_class_i.filename))

                try:
                    sch_info = school_information(school_section=school_section, school_year=school_year,
                                                  classs=classes,
                                                  subject_thought=list_subjecto)
                    CREUD.save_to_database(sch_info)

                # duplication error

                except IntegrityError:
                    duplicated_classes.append(classes)

                # return "'subject::%s'%list_subject"
        if len(duplicated_classes) != 0:
            return "<h1 style='color:red; text-align:center'>the following class already exist for this accademic year in the database" \
                   "</h1><br><h3 style='text-align:center'>" + json.dumps(duplicated_classes) + \
                   "<a href='/ADMIN/GBHS'>go back</a></h3><br>"
        return render_template('administrator.html')

    if number_of_staffs != '':
        staff_section = request.form['staff_section']
        staff_school_year = request.form['staff_school_year']
        duplicate_staff = []

        for i in range(1, int(number_of_staffs) + 1):
            staffs = request.form['staff_name%s' % i].lower()
            ranks = request.form['rank%s' % i]
            if staffs != '' and ranks != '':

                try:
                    staff = staff_information(staff_section=staff_section, school_year=staff_school_year,
                                              staff_name=staffs, rank=ranks)
                    CREUD.save_to_database(staff)
                except IntegrityError:
                    duplicate_staff.append([staffs, ranks])
        if len(duplicate_staff) != 0:
            return "<h1 style='color:red; text-align:center'>the following staff already exist for this accademic year in the database" \
                   "</h1><br><h3 style='text-align:center'>" + str(
                duplicate_staff) + "<a href='/ADMIN/GBHS'>go back</a></h3><br>"
        return render_template('administrator.html')

    number_of_students = request.form['number_of_students']

    if number_of_students != '':
        student_section = request.form['student_section']
        student_school_year = request.form['student_school_year']
        list_student = []
        list_class_student = []
        list_guidant = []
        duplicated_students = []

        for i in range(1, int(number_of_students) + 1):
            student_class = request.form['student_class%s' % i]
            student_name = request.form['student_name%s' % i]
            sex = request.form['student_sex%s' % i]
            student_date_of_birth = request.form['student_date_of_birth%s' % i]
            student_age = request.form['student_age%s' % i]
            guidant = request.form['guidant%s' % i]

            try:
                if student_name != '' and student_class != '' and guidant != '' and student_date_of_birth != '' and student_age != '' and guidant != '':
                    student_inform = student_information(student_section=student_section,
                                                         student_school_year=student_school_year,
                                                         student_name=student_name, student_class=student_class,
                                                         student_date_of_birth=student_date_of_birth, sex=sex,
                                                         student_age=student_age, student_guidant=guidant)
                    CREUD.save_to_database(student_inform)
            except IntegrityError:
                duplicated_students.append([student_name, student_class])

        if len(duplicated_students) != 0:
            return "<h1 style='color:red; text-align:center'>the following student already exist for this accademic year in the database" \
                   "</h1><br><h3 style='text-align:center'>" + str(
                duplicated_students) + "<a href='/ADMIN/GBHS'>go back</a></h3><br>"
        return render_template('administrator.html')
    # except:
    #     return render_template('error page.html', admin_error='block')


@app.route('/api/<school_section>', methods=['GET', 'POST'])
def test(school_section):
    classs = school_information.get_school_information_from_database_school_section(school_section)
    clas = {}
    for i in classs:
        clas.update({i.classs: json.loads(i.subject_thought)})
    return json.dumps(clas)


@app.route("/database_registration", methods=['POST'])
def database_collection():
    nost = request.form['number_of_classes_thought']  # number_of_subject_thought
    staff_name = request.form['teacher_name'].lower()  # ,nost)
    password = request.form['user_set_password']
    class_thought = []
    subject_thought = []
    staff_registered = Database_Registration.get_registration_from_database(staff_name)

    for i in range(1, int(nost) + 1):
        class_th = request.form['class_th%s' % i]
        class_thought.append(class_th)

        subject_th = request.form.getlist('subject_th%s' % i)
        subject_thought.append(subject_th)
    try:
        if staff_registered is None:
            registration_object = Database_Registration(staff_name, password,
                                                        json.dumps(class_thought), json.dumps(subject_thought))
            CREUD.save_to_database(registration_object)
            return render_template('login.html')
        else:
            db.session.rollback()
            return render_template('error page.html', already_register='block', name=staff_name)
    except IntegrityError:
        return render_template('error page.html', name_error='block', name=staff_name)

    # except IntegrityError as e:

    # except:
    #
    # return str(staff_rank)+str(staff_name)+'<br>'+'<h5>'+str(class_thought)+'</h5><br>'+str(subject_thought)


@app.route('/login', methods=['POST','GET'])
def login():
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    if user_name == 'ADMIN' and user_password == 'GBHS012345n6789DZENG':
        return redirect('/ADMIN/GBHS')

    if user_name == 'me' and user_password == 'GBHS012345n6789DZENG':
        return render_template('delete_teacher.html')
    user_name = user_name.lower()
    confirm = Database_Registration.get_registration_from_database_password((user_name), (user_password))
    if confirm is None or confirm.staff_name != (user_name) or confirm.password != (user_password):
        flash(u"Invalid username, please try again.")
        return render_template('login.html', display='block')
    elif confirm.staff_name == user_name and confirm.password == user_password:

        return staff(user_name)

    # except:
    #     return render_template('error page.html')
    # except ERR_CACHE_MISS as e:


# @app.route('/staff/<name>/', methods=['GET', 'POST'])
def staff(name):
    staf = staff_information.get_staff_information()
    school_info = school_information.get_school_information_from_database()
    student_counter = student_information.get_students_in_a_class
    sequence = exam_sequence.get_exam_sequence_from_database()
    school_info = school_information.get_school_information_from_database()
    staff_info = Database_Registration.get_registration_from_database(name)

    for i in staf:

        if i.staff_name == name:

            return render_template('staff.html', sequence=sequence, section=i.staff_section, staff_info=staff_info,
                                   student_amount=student_counter, school_info=school_info, name=name)

    return render_template('error page.html', name=name, name_error='block')


@app.route('/student_result_upload/<name>/<clas>' , methods=['GET','POST'])
def upload(name, clas):
    school_info = school_information.get_school_information_from_database()
    student_data = student_information.get_student_information_from_database()
    student_reload_data_name_list = []
    student_reload_data = subject_and_mark.get_students_report_card()
    for i in student_reload_data:
        student_reload_data_name_list.append(i.student_name)
    student_reload_data_name_list = list(dict.fromkeys(student_reload_data_name_list))
    for i in school_info:
        if i.classs == clas:
            sequence = request.form['sequence%s' % clas]
            subject = request.form['subject%s' % clas]
            term_result(clas=clas, sequence=sequence)
            return render_template('upload.html', student_reload_data_name_list=student_reload_data_name_list,
                                   sequence=sequence, subject=subject, student_reload_data=student_reload_data,
                                   name=name,
                                   clas=clas, student_data=student_data)
    # except:
    #     return render_template('error page.html')

    # class and suject inputed by the secretary stored in a temporal database, validated by the principal and
    # stored in the parmenent database

app.config['UPLOAD_FOLDER'] = 'marks_subjects'

@app.context_processor
def typeo():
    return dict(type=type)


@app.route('/report_database/<name>/<clas>', methods=['POST','GET'])
def report_storing_database(name, clas):
    # student_id = request.form['student_id']
    teacher_name = name
    student_subject = request.form['subject']
    students_class = clas
    sequence = request.form['sequence']
    coefficient = request.form['coefficient']
    file = request.files['marks_file']
    filename = secure_filename(file.filename)

    # import how to create unique names from a list of non unique names
    if filename != '':

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        student_mark = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        for i in range(student_mark.index.size):
            student_name_file = student_mark[student_mark.columns[0]][i]
            mark = student_mark[student_mark.columns[1]][i]
            student_competence_from_file = student_mark[student_mark.columns[2]][i]

            for student in student_information.get_students_in_a_class(classs=clas):
                if student.student_name == student_name_file:

                    if len(student.pupils_name) == 0:
                        if student_name_file != '' and student_competence_from_file != '':
                            student_result = subject_and_mark(student_class=students_class, subject=student_subject,
                                                              student_name=student_name_file, sequence=sequence,
                                                              staff_name=teacher_name,
                                                              mark=mark, coefficient=coefficient,
                                                              competence=student_competence_from_file)
                            CREUD.save_to_database(student_result)
                            break
                    else:
                        for i in range(len(student.pupils_name)):

                            if student.pupils_name[i].student_name == student_name_file and \
                                    student.pupils_name[i].sequence == sequence and \
                                    student.pupils_name[i].subject == student_subject:
                                break

                            elif i == len(student.pupils_name) - 1:

                                if student_name_file != '' and student_competence_from_file != '':

                                    student_result = subject_and_mark(student_class=students_class,
                                                                      subject=student_subject,
                                                                      student_name=student_name_file, sequence=sequence,
                                                                      staff_name=teacher_name, mark=mark,
                                                                      coefficient=coefficient,
                                                                      competence=student_competence_from_file)
                                    CREUD.save_to_database(student_result)
                                else:
                                    continue
    elif filename == '':
        # student_reload_data_name_list = list(dict.fromkeys(student_reload_data_name_list))
        for student in student_information.get_students_in_a_class(classs=clas):
            if student.student_class == clas:

                if len(student.pupils_name) == 0:
                    student_name = request.form['student_name%s' % student.student_name]
                    student_mark = request.form['mark=%s' % student.student_name]
                    student_competence = request.form['competence=%s' % student.student_name]
                    if student_name != '' and student_competence != '':
                        student_result = subject_and_mark(student_class=students_class, subject=student_subject,
                                                          student_name=student_name, sequence=sequence,
                                                          staff_name=teacher_name,
                                                          mark=student_mark, coefficient=coefficient,
                                                          competence=student_competence)
                        CREUD.save_to_database(student_result)
                    else:
                        continue

                else:
                    for i in range(len(student.pupils_name)):

                        if student.pupils_name[i].student_name == student.student_name and \
                                student.pupils_name[i].sequence == sequence and \
                                student.pupils_name[i].subject == student_subject:
                            try:
                                student_name = request.form['student_name%s' % student.student_name]
                                student_mark = request.form['mark=%s' % student.student_name]
                                student_competence = request.form['competence=%s' % student.student_name]
                                if student.pupils_name[i].mark != student_mark:
                                    subject_and_mark.delete_student_with_mark(student=student_name, clas=students_class,
                                                                              sequence=sequence,
                                                                              subject=student_subject)
                                    save = subject_and_mark(student_class=students_class, subject=student_subject,
                                                            student_name=student_name, sequence=sequence,
                                                            staff_name=teacher_name, mark=student_mark,
                                                            coefficient=coefficient,
                                                            competence=student_competence)

                                    CREUD.save_to_database(save)
                                    break
                            except:
                                break

                        elif i == len(student.pupils_name) - 1:
                            student_name = request.form['student_name%s' % student.student_name]
                            student_mark = request.form['mark=%s' % student.student_name]
                            student_competence = request.form['competence=%s' % student.student_name]

                            if student_name != '' and student_competence != '':

                                student_result = subject_and_mark(student_class=students_class, subject=student_subject,
                                                                  student_name=student_name, sequence=sequence,
                                                                  staff_name=teacher_name, mark=student_mark,
                                                                  coefficient=coefficient,
                                                                  competence=student_competence)
                                CREUD.save_to_database(student_result)
                            else:
                                continue

    return staff(name=name)

    # except:
    #     return render_template('error page.html',error_storing_result='block')


@app.route('/student', methods=['GET', 'POST'])
def sequence_selection():
    try:
        sequences = exam_sequence.get_exam_sequence_from_database()
        return render_template('sequence.html', sequences=sequences)
    except:
        return render_template('error page.html', evaluation_has_not_been_inputed='block')

@app.route('/student/<sequence>', methods=['GET','POST'])
def result(sequence):
    student_info = student_information.get_student_information_from_database()
    school_info = school_information.get_school_information_from_database()
    report = subject_and_mark.get_students_report_card()
    return render_template('result.html', sequence=sequence, student_info=student_info, school_info=school_info, report=report)


@app.route('/report/<clas>/<sequence>')
def student__class_report(clas, sequence):
    students = student_information.get_student_information_from_database()
    student_list = []
    try:
        for student in students:

            if student.student_class == clas:
                student_list.append(student)
        return render_template('student_exam_list.html', sequence=sequence, student=student_list)
    except:
        return render_template('error page.html', classs_info='block')

def calculating_position(clasor, sequen):

    results = subject_and_mark.get_class_with_results(clas=clasor, sequence=sequen)
    class_of_result = student_information.get_students_in_a_class(classs=clasor)
    total_info =save_student_total_mark.get_class_student(clas=clasor,sequence=sequen)
    for student in class_of_result:
        total_mark = 0
        total_coefficient = 0
        if len(total_info) == 0:

            for result in results:
                if result.student_name == student.student_name and result.sequence == sequen:
                    total_mark = total_mark + (result.coefficient * result.mark)
                    total_coefficient = total_coefficient + (result.coefficient)
            save = save_student_total_mark(student_name=student.student_name, total_student_coeff=total_coefficient,
                                           sequence=sequen, student_class=student.student_class, student_mark=total_mark)

            CREUD.save_to_database(save)
        for i in range(len(total_info)):

            if total_info[i].student_name == student.student_name and total_info[i].sequence == sequen and \
                    total_info[i].student_class == clasor:
                save_student_total_mark.delete_student_with_mark(student=student.student_name, clas=clasor,
                                                                 sequence=sequen)

                for result in results:
                    if result.student_name == student.student_name and result.sequence == sequen:
                        total_mark = total_mark + result.coefficient*result.mark
                        total_coefficient = total_coefficient + result.coefficient
                save = save_student_total_mark(student_name=student.student_name,
                                               total_student_coeff=total_coefficient,sequence=sequen,
                                               student_class=student.student_class,student_mark=total_mark)
                CREUD.save_to_database(save)
                break

            if i == len(total_info) - 1:
                for result in results:
                    if result.student_name == student.student_name and result.sequence == sequen:
                        total_mark = total_mark + (result.coefficient * result.mark)
                        total_coefficient = total_coefficient + (result.coefficient)
                save = save_student_total_mark(student_name=student.student_name,
                                                total_student_coeff=total_coefficient, sequence=sequen,
                                               student_class=student.student_class, student_mark=total_mark)
                CREUD.save_to_database(save)

    class_mark_aver = 0
    class_total_coeff = 0
    total = save_student_total_mark.get_class_student(clas=clasor, sequence=sequen)
    for pupil in total:
        class_mark_aver = class_mark_aver + int(pupil.student_mark)
        class_total_coeff = class_total_coeff + pupil.total_student_coeff
    class_aver = class_mark_aver/class_total_coeff

    return [[total, class_aver]]


def term_result(clas, sequence):
    results = subject_and_mark.get_class_only(clas=clas)
    resul = subject_and_mark.get_class_with_results(clas=clas, sequence=sequence)

    if sequence == 'First term|Premiere tremestre' or sequence == 'Second Term|Deuxieme tremestre' or \
            sequence == 'Third term|Troisieme tremestre':

        for result in results:
            for student in results:

                if sequence == 'First term|Premiere tremestre':
                    if result.sequence == '1' and student.sequence == '2' and result.subject == student.subject and \
                            result.student_name == student.student_name:
                        if subject_and_mark.get_class_subject_sequence_student(clas=clas, sequence=sequence,
                                                                               subject=result.subject,
                                                                               name=student.student_name) is None:

                            mark = (float(result.mark) + float(student.mark)) / 2
                            save = subject_and_mark(student_class=clas, student_name=student.student_name,
                                                    sequence=sequence, \
                                                    staff_name=student.staff_name, subject=student.subject, mark=mark,
                                                    coefficient=student.coefficient,
                                                    competence=student.competence + result.competence)
                            CREUD.save_to_database(save)
                            break
                        else:

                            mark = (float(result.mark) + float(student.mark)) / 2
                            subject_and_mark.get_class_subject_sequence_student(clas=clas, sequence=sequence,
                                                                                subject=result.subject,
                                                                                name=student.student_name).mark = mark
                            db.session.commit()
                            break
                if sequence == 'Second Term|Deuxieme tremestre':
                    if result.sequence == '3' and student.sequence == '4' and result.subject == student.subject and \
                            result.student_name == student.student_name:
                        if subject_and_mark.get_class_subject_sequence_student(clas=clas, sequence=sequence,
                                                                               subject=result.subject,
                                                                               name=student.student_name) is None:

                            mark = (float(result.mark) + float(student.mark)) / 2
                            save = subject_and_mark(student_class=clas, student_name=student.student_name,
                                                    sequence=sequence, staff_name=student.staff_name,
                                                    subject=student.subject, mark=mark,
                                                    coefficient=student.coefficient,
                                                    competence=student.competence + result.competence)
                            CREUD.save_to_database(save)
                            break
                        else:
                            mark = (float(result.mark) + float(student.mark)) / 2
                            subject_and_mark.get_class_subject_sequence_student(clas=clas, sequence=sequence,
                                                                                subject=result.subject,
                                                                                name=student.student_name).mark = mark
                            db.session.commit()
                            break

                if sequence == 'Third term|Troisieme tremestre':
                    if result.sequence == '5' and student.sequence == '6' and result.subject == student.subject and \
                            result.student_name == student.student_name:
                        if subject_and_mark.get_class_subject_sequence_student(clas=clas, sequence=sequence,
                                                                               subject=result.subject,
                                                                               name=student.student_name) is None:

                            mark = (float(result.mark) + float(student.mark)) / 2
                            save = subject_and_mark(student_class=clas, student_name=student.student_name,
                                                    sequence=sequence, \
                                                    staff_name=student.staff_name, subject=student.subject, mark=mark,
                                                    coefficient=student.coefficient,
                                                    competence=student.competence + result.competence)
                            CREUD.save_to_database(save)
                            break
                        else:

                            mark = (float(result.mark) + float(student.mark)) / 2
                            subject_and_mark.get_class_subject_sequence_student(clas=clas, sequence=sequence,
                                                                                subject=result.subject,
                                                                                name=student.student_name).mark = mark
                            db.session.commit()
                            break


    # except:
    #     return render_template('error page.html')


def annual_average(clas, sequence):
    if sequence == 'Third term|Troisieme tremestre':

        students_result = save_student_total_mark.get_class_report_card(clas=clas)
        if students_result is None:
            return render_template('error page.html')

        else:
            for stud_sque in students_result:
                user_student = annual_performance.get_student_annual_result(stud_sque.student_name, clas=clas)
                if user_student is None:
                    firstevaluation = 0
                    secondevaluation = 0
                    thirdevaluation = 0
                    for stuc in students_result:
                        if stuc.student_name == stud_sque.student_name:
                            if stuc.sequence == 'First term|Premiere tremestre':
                                firstevaluation = int(stuc.student_mark)

                            elif stuc.sequence == 'Second Term|Deuxieme tremestre':
                                secondevaluation = int(stuc.student_mark)

                            elif stuc.sequence == 'Third term|Troisieme tremestre':
                                thirdevaluation = int(stuc.student_mark)

                    total = firstevaluation + secondevaluation + thirdevaluation

                    save = annual_performance(student_name=stud_sque.student_name, student_clas=clas,
                                              firstevaluation=firstevaluation, secondevaluation=secondevaluation,
                                              thirdevaluation=thirdevaluation,student_annual_mark=total,
                                              student_total_coefficient=stud_sque.total_student_coeff)
                    CREUD.save_to_database(save)
                if user_student is not None:
                    annual_performance.delete_student_annual_result(student_name=stud_sque.student_name, student_class=clas)
                    firstevaluation = 0
                    secondevaluation = 0
                    thirdevaluation = 0
                    for stuc in students_result:
                        if stuc.student_name == stud_sque.student_name:
                            if stuc.sequence == 'First term|Premiere tremestre':
                                firstevaluation = int(stuc.student_mark)


                            if stuc.sequence == 'Second Term|Deuxieme tremestre':
                                secondevaluation = int(stuc.student_mark)


                            if stuc.sequence == 'Third term|Troisieme tremestre':
                                thirdevaluation = int(stuc.student_mark)

                    total = firstevaluation + secondevaluation + thirdevaluation
                    save = annual_performance(student_name=stud_sque.student_name, student_clas=clas,
                                              firstevaluation=firstevaluation, secondevaluation=secondevaluation,
                                              thirdevaluation=thirdevaluation, student_annual_mark=total,
                                              student_total_coefficient=stud_sque.total_student_coeff)
                    CREUD.save_to_database(save)


@app.route('/student_result/<student_name>/<clas>/<sequence>')
def student_report(student_name, clas,sequence):
        student_report_card = subject_and_mark.get_students_report_card()
        student_class_report = subject_and_mark.get_class_and_subject_and_sequence_list
        class_info = school_information.get_school_information_from_database()
        student_i = student_information.get_students_in_a_class(classs=clas)
        student_list = []

        term_result(clas=clas, sequence=sequence)
        position = calculating_position

        for student_rep in student_report_card:
            if student_rep.student_name == student_name:
                student_list.append(student_rep)

        annual_average(clas=clas, sequence=sequence)

        annuel_resulter = annual_performance.get_annual_result(clas=clas)
        try:
            return render_template('report_card.html', position=position, sequence=sequence, student_inf2=student_i,
                                   student_name=student_name, students_info=student_report_card, classs=clas,
                                   clas=class_info, student_class_report=student_class_report,
                                   annuel_resulter=annuel_resulter)
        except ZeroDivisionError:
            return render_template('error page.html', no_mark_ready='block', evaluation=sequence)

@app.route('/delete_staff', methods=['GET', 'POST'])
def delete_staff():

    staff_name = request.form['staff_name']
    try:
        subject_and_mark.delete_teacher_and_mark(staff_name)
    except UnmappedInstanceError:
        pass
    try:
        Database_Registration.delete_teacher_from_registration(staff_name)
    except UnmappedInstanceError:
        pass
    try:
        staff_information.delete_staff_from_database(staff_name)
        return render_template('delete_teacher.html')
    except UnmappedInstanceError:
        return render_template('delete_teacher.html')

if __name__ == '__main__':
    app.run(host='192.168.43.7', port=10000, use_reloader=True, debug=True, threaded=True)
    # app.run(host='127.0.0.1', port=60000, use_reloader=True, debug=True)
    # app.run(host='192.168.43.220', port=10000, use_reloader=True, debug=True, threaded=True)
    # UI.run()


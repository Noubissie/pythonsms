from flask import Flask ,render_template
import pdfkit
import jinja2
import json
import os
import pandas as pd

from flask import render_template, request, session, url_for, redirect, flash
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
from sqlalchemy.orm.exc import UnmappedInstanceError
#from flaskwebgui import FlaskUI
from database_head import app, db
from database import Database_Registration, CREUD, school_information,  staff_information, student_information, \
    subject_and_mark, exam_sequence, save_student_total_mark, annual_performance
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
@app.context_processor
def length():
    return dict(length=len)
# templateLoader = jinja2.FileSystemLoader(searchpath="templates")
# templateEnv = jinja2.Environment(loader=templateLoader)
# TEMPLATE_FILE = "form 1.html"
# template = templateEnv.get_template(TEMPLATE_FILE)
# output = template.render(i=[1,2,3,4,5,6])
#
# # f = open("test.html", "w+")
# with open("form 1.html", "w+") as myfile:
#     myfile.write(output)
# pdfkit.from_file("form 1.html", "form 1.pdf")
# print(output)





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

@app.route("/")
def hoope():
    return render_template("test.html")
if __name__ == '__main__':
    app.run(host='192.168.43.7', port=11000, use_reloader=True, debug=True, threaded=True)
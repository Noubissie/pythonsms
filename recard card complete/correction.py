from database import subject_and_mark, exam_sequence, school_information, student_information, CREUD
from database_head import app, db
from flask import render_template, redirect, url_for, request
import json

app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route("/<clas>/<seq>")
def hope(clas, seq):
    # print('clas:::::',clas)
    marks = subject_and_mark.get_class_with_results(clas, seq)
    if(marks):
        a = {}
        coef = 1
        staff = "//"
        for student_m in marks:
            a[student_m.student_name] = []
            coef = student_m.coefficient
            staff = student_m.staff_name
        for student_m in marks:
            a[student_m.student_name].append(student_m.subject.upper().strip())

        student_personal_subject_dic = a
        # print(student_personal_subject_dic)
        # sequence = exam_sequence.get_exam_sequence_from_database()
        students_in_class = student_information.get_students_in_a_class(clas)
        # print('student', school_information.change_subjects_of_a_class(clas).subject_thought.upper())
        subject = sorted(json.loads(school_information.change_subjects_of_a_class(clas).subject_thought))
        new_subject = []
        for i in subject:
            new_subject.append(i.upper())
        subject = new_subject
    #    print(marks)

        return render_template("admin_correction_sheet.html", seq=seq, marks=marks, spsd=student_personal_subject_dic,
                               subjects=subject, students=students_in_class, clas=clas, coef=coef, staff=staff)
    else:
        return "nothing present for you yet"


@app.route("/marksheet/<clas>/<seq>/<coef>", methods=["POST"])
def marksheet(clas, seq, coef):
    student_class = student_information.get_students_in_a_class(clas)
    subjects = sorted(json.loads(school_information.change_subjects_of_a_class(clas).subject_thought))

    for student in student_class:
        student_name = request.form["%s" % student.student_name]
        for subject in subjects:
            student_mark = request.form["%s%s%s" % (student_name.upper(), subject.upper(), seq)]
            if (student_mark != ""):
                # print(student_name, " ", subject, " ", student_mark)
                new_mark = subject_and_mark.get_class_subject_sequence_student(clas=clas, sequence=seq, subject=subject, name=student_name)
                if new_mark:
                    new_mark.mark = student_mark
                    db.session.commit()
                else:
                    staff_group = subject_and_mark.get_class_and_subject_and_sequence_list(clas=clas,sequence=seq,subject=subject)
                    # test = subject_and_mark.get_class_and_subject_and_sequence_name(clas=clas, sequence=seq, subject=subject,name="john Paul Ewo")
                    # print("test::",test)
                    print("staff_group::",staff_group)
                    if len(staff_group)==0:
                        for i in range(1, 5):
                            staff_group = subject_and_mark.get_class_and_subject_and_sequence_list(clas=clas, sequence=i, subject=subject)
                            if len(staff_group) != 0:
                                break
                            elif i == 4:
                                return "input your mark from your personal site"

                    staff = staff_group[0].staff_name
                    # if subject == "Mathematics":
                    #     staff = "noubissie"
                    save = subject_and_mark(student_class=clas, student_name=student_name, sequence=seq,
                                        staff_name=staff, subject=subject, mark=student_mark, coefficient=coef,
                                        competence="//")
                    CREUD.save_to_database(save)
            else:
                pass
                # print(f"{subject} ,is not available with mark {student_name}")

    marks = subject_and_mark.get_class_with_results(clas, seq)
    a = {}
    for student_m in marks:
        a[student_m.student_name] = []
    for student_m in marks:
        a[student_m.student_name].append(student_m.subject.upper().strip())

    student_personal_subject_dic = a
    sequence = exam_sequence.get_exam_sequence_from_database()
    students_in_class = student_information.get_students_in_a_class(clas)

    new_subject = []
    for i in subjects:
        new_subject.append(i.upper())
    subject1 = new_subject

    return render_template("correction.html", seq=seq, marks=marks, spsd=student_personal_subject_dic, subjects=subject1,
                           students=students_in_class, clas=clas)


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=8080, debug=True)

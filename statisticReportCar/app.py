from flask import session, render_template,sessions,url_for
from database_head import app
from database import resultAverage, CREUD, save_student_total_mark,trimestrialAverage
from statistics import mean


@app.route("/")
def index():
    # print("length::", len(save_student_total_mark.get_result_by_sequence(sequence=2)))
    for i in save_student_total_mark.get_result_by_sequence(sequence=3):

        try:
            print("total student coef", i.total_student_coeff)
            average20 = i.student_mark/i.total_student_coeff
            resultAvg = resultAverage(student_name=i.student_name, clas=i.student_class, sequence=i.sequence, average20=average20)
            CREUD.save_to_database(resultAvg)
        except ZeroDivisionError:
            print("*******************division by zero****************************************************")
            print("student class", i.student_name)
            print("***********************************************************************")
            # except:
            #     print("**************any exception*********************************************************")
            #     print("student class", i.student_name)
            #     print("***********************************************************************")
    # return render_template("statistic.html", student=resultAverage.get_resultAverage(clas="Form 1", sequence=1))
    return "it is done"

# @app.route("/")
# def index():
#     # print("length::", len(save_student_total_mark.get_result_by_sequence(sequence=2)))
#
#     for i in resultAverage.get_result_by_sequence(sequence=4):
#         try:
#             trimestrialresult = mean([resultAverage.get_studentResultAverage_by_sequence(
#                 student_name=i.student_name, sequence=3).average20,
#                                           resultAverage.get_studentResultAverage_by_sequence(
#                                               student_name=i.student_name, sequence=3).average20])
#             print("total student coef", i.student_name)
#             trimesAvg = resultAverage(student_name=i.student_name, clas=i.clas, sequence="Second Term|Deuxieme tremestre", average20=trimestrialresult)
#             CREUD.save_to_database(trimesAvg)
#         except AttributeError:
#             print("*******************division by zero****************************************************")
#             print("student class", i.student_name)
#             print("***********************************************************************")
#             # except:
#             #     print("**************any exception*********************************************************")
#             #     print("student class", i.student_name)
#             #     print("***********************************************************************")
#     # return render_template("statistic.html", student=resultAverage.get_resultAverage(clas="Form 1", sequence=1))
#     return "it is done"


# @app.route("/")
# def index():
#     average = resultAverage.get_resultAverage(clas="Form 1", sequence=2)
#     passcount = len(list(filter(lambda x: x >= 10.0, [student.average20 for student in average])))
#
#     return render_template("statistic.html", student_average=average, passcount=passcount)


#STATISTIC PER CLASS

# @app.route("/<clas>")
# def index(clas):
#
#     def averageformular(seq):
#         average = resultAverage.get_resultAverage(clas=clas, sequence=seq)
#         passcount = len(list(filter(lambda x: x >= 10.0, [student.average20 for student in average])))
#         sequence = seq
#         numberOfStudents = len(average)
#         percentage_pass = (passcount / len(average)) * 100
#         percentageFail = (1 - (passcount/ len(average))) * 100
#         bestStudent = average[0].student_name
#         bestStudentAverage = average[0].average20
#         lastStudent = average[len(average) - 1].student_name
#         lastStudentAverage = average[len(average) - 1].average20
#         return sequence, numberOfStudents, round(percentage_pass, 2), round(percentageFail, 2), bestStudent, \
#                round(bestStudentAverage, 2), lastStudent, round(lastStudentAverage, 2)
#
#     clas = clas
#
#     s = [3, 4, "Second Term|Deuxieme tremestre"]
#
#     return render_template("statistic.html",test=list(map(averageformular, s)), clas=clas)
#     # return render_template("statistic.html", student_average=average, passcount=passcount)



# ENTIRE SCHOOL STATISTIC

# @app.route("/")
# def index():
#
#     def averageformular(seq):
#         average = resultAverage.get_result_by_sequence(seq)
#         passcount = len(list(filter(lambda x: x >= 10.0, [student.average20 for student in average])))
#         sequence = seq
#         numberOfStudents = len(average)
#         percentage_pass = (passcount / len(average)) * 100
#         percentageFail = (1 - (passcount/ len(average))) * 100
#         bestStudent = average[0].student_name
#         bestStudentClass = average[0].clas
#         bestStudentAverage = average[0].average20
#         lastStudent = average[len(average) - 1].student_name
#         lastStudentClass = average[len(average) - 1].clas
#         lastStudentAverage = average[len(average) - 1].average20
#         return sequence, numberOfStudents, round(percentage_pass, 2), round(percentageFail, 2), bestStudent, \
#                bestStudentClass, round(bestStudentAverage, 2), lastStudent, lastStudentClass,\
#                round(lastStudentAverage, 2)
#
#     s = [1, 2, "First term|Premiere tremestre"]
#
#     return render_template("statistic.html",test=list(map(averageformular, s)), clas="LYCEE BILINGUE DE DZENG PREMIERE TREMESTRE")


# French section

# @app.route("/")
# def index():
#
#     def averageformular(seq):
#         average1 = resultAverage.get_result_by_sequence(seq)
#
#         def h(x):
#             x = x.clas
#             # if x != "Form 1" and x != "Form 2" and x != "Form 3" and x != "Form 4 Science" and x != "Form Arts" and x != "Form 5 Arts" and x != "Form 5 Science":
#             if x == "Form 1" or x == "Form 2" or x == "Form 3" or x == "Form 4 Science" \
#                     or x == "Form 4 Arts":
#                 # if x == "Form 1" or x == "Form 2" or x == "Form 3" or x == "Form 4 Science" \
#                 #         or x == "Form 4 Arts" or x == "Form 5 Arts" or x == "Form 5 Science":
#                 return x
#         average = list(filter(h, average1))
#         # print("********************************************")
#         # print(average)
#         # print("********************************************")
#         passcount = len(list(filter(lambda x: x >= 10.0, [student.average20 for student in average])))
#         sequence = seq
#         numberOfStudents = len(average)
#         percentage_pass = (passcount / len(average)) * 100
#         percentageFail = (1 - (passcount/ len(average))) * 100
#         bestStudent = average[0].student_name
#         bestStudentClass = average[0].clas
#         bestStudentAverage = average[0].average20
#         lastStudent = average[len(average) - 1].student_name
#         lastStudentClass = average[len(average) - 1].clas
#         lastStudentAverage = average[len(average) - 1].average20
#         return sequence, numberOfStudents, round(percentage_pass, 2), round(percentageFail, 2), bestStudent, \
#                bestStudentClass, round(bestStudentAverage, 2), lastStudent, lastStudentClass,\
#                round(lastStudentAverage, 2)
#
#     s = [3, 4, "Second Term|Deuxieme tremestre"]
#
#     return render_template("statistic.html", test=list(map(averageformular, s)), clas="LYCEE BILINGUE DE DZENG Deuxieme Tremestre section anglophone")


if __name__ == "__main__":
    app.run()
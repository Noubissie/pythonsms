from database_head import db  # , app
# import flask_whooshalchemy as wa
# from whoosh.analysis import StemmingAnalyzer



class subject_and_mark(db.Model):
    __tablename__ = 'subject_and_mark'
    id_ = db.Column('id_', db.Integer, primary_key=True)
    student_class = db.Column('student_class',db.String(200),db.ForeignKey('school_information.classs'))
    student_name = db.Column('student_name', db.String(200), db.ForeignKey('student_information.student_name'))
    sequence = db.Column('sequence', db.String(200), db.ForeignKey('exam_sequence.sequence'))
    staff_name = db.Column('staff_name', db.String(200), db.ForeignKey('staff_information.staff_name'))
    subject = db.Column('subject', db.String(200))
    mark = db.Column('mark', db.Float)
    coefficient = db.Column('coefficient', db.Integer)
    competence = db.Column('competence', db.String(1000))

    def __init__(self, student_class, student_name, sequence, staff_name, subject, mark, coefficient, competence):
        # self.id_ = id_
        self.student_class = student_class
        self.student_name = student_name
        self.sequence = sequence
        self.staff_name = staff_name
        self.subject = subject
        self.mark = mark
        self.coefficient = coefficient
        self.competence = competence


    @staticmethod
    def get_students_report_card():
        return subject_and_mark.query.all()

    @staticmethod
    def get_class_only(clas):
        return subject_and_mark.query.filter_by(student_class=clas).all()

    @staticmethod
    def get_class_with_results(clas, sequence):
        return subject_and_mark.query.filter_by(student_class=clas, sequence=sequence).all()

    @staticmethod
    def get_class_and_subject_and_sequence_list(clas,sequence,subject):
        return subject_and_mark.query.filter_by(student_class=clas, sequence=sequence,
                                                subject=subject).order_by(subject_and_mark.mark.desc()).all()
    @staticmethod
    def get_class_subject_sequence_student(clas, sequence, subject, name):
        return subject_and_mark.query.filter_by(student_class=clas, sequence=sequence, subject=subject,
                                                 student_name=name).first()

    @staticmethod
    def get_student_offering_particular_subject(subject):
        return subject_and_mark.query.filter_by(subject=subject).all()

    @staticmethod
    def get_particular_student(student):
        return subject_and_mark.query.filter_by(student_name=student).all()

    @staticmethod
    def delete_student_with_mark(student, clas, sequence,subject):
        a = subject_and_mark.query.filter_by(student_name=student, student_class=clas,
                                                    sequence=sequence, subject=subject).first()
        db.session.delete(a)
        db.session.commit()

    @staticmethod
    def delete_student(student):
        a = subject_and_mark.query.filter_by(student_name=student).all()
        for i in a:
            db.session.delete(i)
            db.session.commit()

    @staticmethod
    def delete_teacher_and_mark(staff_name):
        delete = subject_and_mark.query.filter_by(staff_name=staff_name).all()
        for i in delete:
            db.session.delete(i)
            db.session.commit()


class save_student_total_mark(db.Model):
    __tablename__ = 'save_student_total_mark'
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_name = db.Column(db.String(200))
    student_class = db.Column(db.String(200))
    student_mark =db.Column(db.Float)
    total_student_coeff = db.Column(db.Float)
    sequence = db.Column(db.String(200))

    def __init__(self, student_name,total_student_coeff, sequence, student_class,student_mark):
        self.student_name = student_name
        self.student_class = student_class
        self.student_mark = student_mark
        self.sequence = sequence
        self.total_student_coeff = total_student_coeff

    @staticmethod
    def get_total_mark():
        return save_student_total_mark.query.all()

    @staticmethod
    def get_class_student(clas, sequence):
        return save_student_total_mark.query.filter_by(student_class=clas,
                                                       sequence=sequence).order_by(save_student_total_mark.student_mark.desc()).all()

    @staticmethod
    def get_particular_student(student):
        return save_student_total_mark.query.filter_by(student_name=student).all()


    @staticmethod
    def delete_student_with_mark(student, clas, sequence):
        a = save_student_total_mark.query.filter_by(student_name=student, student_class=clas,
                                                sequence=sequence).first()
        db.session.delete(a)
        db.session.commit()

    @staticmethod
    def delete_student(student):
        a = save_student_total_mark.query.filter_by(student_name=student).all()
        for i in a:
            db.session.delete(i)
            db.session.commit()


class annual_performance(db.Model):
    __tablename__ = 'annual_performance'
    student_name = db.Column(db.String(200), primary_key=True)
    student_class = db.Column(db.String(200))
    firstevaluation = db.Column(db.Float)
    secondevaluation = db.Column(db.Float)
    thirdevaluation = db.Column(db.Float)
    student_annual_mark = db.Column(db.Float)
    student_total_coefficient = db.Column(db.Integer)

    def __init__(self, student_name, student_clas, firstevaluation, secondevaluation, thirdevaluation,student_annual_mark,\
                 student_total_coefficient):
        self.student_name = student_name
        self.student_class = student_clas
        self.firstevaluation = firstevaluation
        self.secondevaluation = secondevaluation
        self.thirdevaluation = thirdevaluation
        self.student_annual_mark = student_annual_mark
        self.student_total_coefficient = student_total_coefficient

    @staticmethod
    def get_annual_result(clas):
        return annual_performance.query.filter_by(student_class=clas).order_by(annual_performance.student_annual_mark.desc()).all()

    @staticmethod
    def get_student_annual_result(student_name,clas):
        return annual_performance.query.filter_by(student_name=student_name, student_class=clas).first()

    @staticmethod
    def get_particular_student(student):
        return annual_performance.query.filter_by(student_name=student).all()

    @staticmethod
    def delete_student_annual_result(student_name, student_class):
        a = annual_performance.query.filter_by(student_name=student_name,student_class=student_class).first()
        db.session.delete(a)
        db.session.commit()

    @staticmethod
    def delete_student(student):
        a = annual_performance.query.filter_by(student_name=student).all()
        for i in a:
            db.session.delete(i)
            db.session.commit()

class school_information(db.Model):
    __tablename__ = 'school_information'
    school_section = db.Column(db.String(200))
    school_year = db.Column(db.String(200))
    classs = db.Column(db.String(200), primary_key=True)
    subject_thought = db.Column(db.String(5000))
    pupils_class = db.relationship('subject_and_mark', backref=db.backref('class'))

    def __init__(self, school_section, school_year, classs, subject_thought):
        self.school_section = school_section
        self.school_year = school_year
        self.classs = classs
        self.subject_thought = subject_thought

    @staticmethod
    def get_school_information_from_database():
        return school_information.query.all()

    @staticmethod
    def get_school_information_from_database_school_section(school_section):
        return school_information.query.filter_by(school_section=school_section).all()

    @staticmethod
    def change_subjects_of_a_class(clas):
        return school_information.query.filter_by(classs=clas).first()

class staff_information(db.Model):
    __tablename__ = 'staff_information'
    staff_section = db.Column(db.String(200))
    school_year = db.Column(db.String(200))
    staff_name = db.Column(db.String(200), primary_key=True)
    rank = db.Column(db.String(200))

    staff_school = db.relationship('subject_and_mark', backref=db.backref('teacher'))

    def __init__(self, staff_section, school_year, staff_name, rank):
        self.staff_section = staff_section
        self.school_year = school_year
        self.staff_name = staff_name
        self.rank = rank

    @staticmethod
    def get_staff_information():
        return staff_information.query.all()

    @staticmethod
    def delete_staff_from_database(staff_name):
        delete = staff_information.query.filter_by(staff_name=staff_name).first()
        db.session.delete(delete)
        db.session.commit()

class Database_Registration(db.Model):
    # DEFAULT_WHOOSH_INDEX_NAME = 'whoosh_index'
    __tablename__ = 'registration_database'
    # __searchable__ = ['staff_name', 'password']   # the columns to be searcbed
    # __analyzer__ = StemmingAnalyzer()
    id = db.Column(db.Integer, primary_key=True)
    staff_in = db.relationship('staff_information')
    staff_name = db.Column(db.String(200), db.ForeignKey('staff_information.staff_name'))
    password = db.Column(db.Text(32*1024))
    class_thought = db.Column('class_thought', db.String(200))
    subject_thought = db.Column('subject_thought', db.String(200))

    def __init__(self, staff_name, password, class_thought, subject_thought):
        self.staff_name = staff_name
        self.password = password
        self.class_thought = class_thought
        self.subject_thought = subject_thought

    @staticmethod
    def get_registration_from_database(name):
        # the filter element get the data from the database that posses any of the character listed in its search item,
        # could be one or both
        # it is an or operator
        return Database_Registration.query.filter_by(staff_name=name).first()

    @staticmethod
    def get_registration_from_database_password(user_name, user_password):
        return Database_Registration.query.filter_by(staff_name=user_name,password=user_password).first()
    @staticmethod
    def get_every_registrated_staff():
        return Database_Registration.query.all()

    @staticmethod
    def delete_teacher_from_registration(staff_name):
        delete = Database_Registration.query.filter_by(staff_name=staff_name).first()
        db.session.delete(delete)
        db.session.commit()

class student_information(db.Model):
    __tablename__ = 'student_information'
    student_section = db.Column(db.String(200))
    student_school_year = db.Column(db.String(200))
    student_name = db.Column(db.String(200), primary_key=True)
    student_class = db.Column(db.String(200))
    student_date_of_birth = db.Column(db.Date)
    student_sex = db.Column(db.String(4))
    student_age = db.Column(db.Integer)
    student_guidant = db.Column(db.String(200))
    pupils_name = db.relationship('subject_and_mark', backref=db.backref('pupils_name'))

    def __init__(self,student_section, student_school_year, student_name, student_class, student_date_of_birth, sex,
                 student_age, student_guidant):
        self.student_section = student_section
        self.student_school_year = student_school_year
        self.student_name = student_name
        self.student_class = student_class
        self.student_date_of_birth = student_date_of_birth
        self.student_age = student_age
        self.student_sex = sex
        self.student_guidant = student_guidant

    @staticmethod
    def get_student_information_from_database():
        return student_information.query.all()

    @staticmethod
    def get_students_in_a_class(classs):
        return student_information.query.filter_by(student_class=classs).order_by(student_information.student_name).all()

    @staticmethod
    def get_particular_student(student):
        return student_information.query.filter_by(student_name=student).first()

    @staticmethod
    def delete_student(student):
        delete = student_information.query.filter_by(student_name=student).first()
        db.session.delete(delete)
        db.session.commit()

class exam_sequence(db.Model):

    __tablename__ = 'exam_sequence'
    sequence = db.Column(db.String(200), primary_key=True)
    pupils_sequence = db.relationship('subject_and_mark', backref=db.backref('pupils_sequence'))

    def __init__(self, sequence):
        self.sequence = sequence

    @staticmethod
    def get_exam_sequence_from_database():
        return exam_sequence.query.all()

    @staticmethod
    def delete_exam_sequence(sequence):
        delete = exam_sequence.query.filter_by(sequence=sequence).all()
        for i in delete:
            db.session.delete(i)
            db.session.commit()


class CREUD:

    @staticmethod
    def save_to_database(table_object):
        # db.drop_all()
        db.create_all()
        db.session.add(table_object)
        db.session.commit()


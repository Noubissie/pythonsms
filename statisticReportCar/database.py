from database_head import db


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
    def get_result_by_sequence(sequence):
        return save_student_total_mark.query.filter_by(sequence=sequence).all()
    @staticmethod
    def get_particular_student(student):
        return save_student_total_mark.query.filter_by(student_name=student).all()


    @staticmethod
    def delete_student_with_mark(student, clas, sequence):
        a = save_student_total_mark.query.filter_by(student_name=student, student_class=clas, sequence=sequence).first()
        db.session.delete(a)
        db.session.commit()

    @staticmethod
    def delete_student(student):
        a = save_student_total_mark.query.filter_by(student_name=student).all()
        for i in a:
            db.session.delete(i)
            db.session.commit()


class resultAverage(db.Model):
    __bind_key__ = "one"
    __tablename__ = "resultAverage"
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(500))
    clas = db.Column(db.String(500))
    sequence = db.Column(db.String(500))
    average20 = db.Column(db.Float)

    def __init__(self, student_name, clas, sequence,average20):
        self.student_name = student_name
        self.clas = clas
        self.sequence = sequence
        self.average20 = average20

    @staticmethod
    def get_resultAverage(clas, sequence):
        return resultAverage.query.filter_by(clas=clas, sequence=sequence).order_by(resultAverage.average20.desc()).all()

    @staticmethod
    def get_result_by_sequence(sequence):
        return resultAverage.query.filter_by(sequence=sequence).order_by(resultAverage.average20.desc()).all()

    @staticmethod
    def get_studentResultAverage_by_sequence(student_name, sequence):
        return resultAverage.query.filter_by(student_name=student_name, sequence=sequence).first()


class trimestrialAverage(db.Model):
    __bind_key__ = "one"
    __tablename__ = "trimestrialAverage"
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(500))
    clas = db.Column(db.String(500))
    sequence = db.Column(db.String(500))
    average20 = db.Column(db.Float)

    def __init__(self, student_name, clas, sequence, average20):
        self.student_name = student_name
        self.clas = clas
        self.sequence = sequence
        self.average20 = average20

    @staticmethod
    def get_trimestrialAverage(clas, sequence):
        return trimestrialAverage.query.filter_by(clas=clas, sequence=sequence).order_by(trimestrialAverage.average20.desc()).all()


# class statisticals(db.Model):
#     __bind_key__ = "one"
#     __tablename__ = "trimestrialAverage"
#     id = db.Column(db.Integer, primary_key=True)
#     student_name = db.Column(db.String(500))
#     clas = db.Column(db.String(500))
#     term = db.Column(db.String(500))
#     totalaverage20 = db.Column(db.Float)
class CREUD:

    @staticmethod
    def save_to_database(table_object):
        db.create_all()
        db.session.add(table_object)
        db.session.commit()

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['mydb']

emp = db['emp']


#
# def get_emps():
#     emps = emp.find()
#     for e in emps:
#         print(e['_id'], ',', e['ename'], ',', e['job'], ',', e['sal'])
#
#
# get_emps()
#
#
# def get_Managers():
#     criteria = {'job': 'MANAGERS'}
#     emps = emp.find(criteria)
#     for e in emps:
#         # if e['sal'] is None:
#         #     e['sal'] == 0.0
#         print(e['_id'], e['ename'], e['job'], e['sal'])
#
#
# get_Managers()


# def addNewEmp():
#     newEmp = ({'_id': 101, 'ename': 'nita', 'job': 'Manager', 'sal': 2000, 'deptno': 20})
#     emp.insert_one(newEmp)
#     print('emp inserted....')
#
# addNewEmp()


# def deleteEmp():
#     empid = int(input("enter emp id to delete from database: "))
#     name = {'ename': 'SMITH'}
#     name_emp = emp.find(name)
#     emp.delete_one({'_id': empid})
#     print(f"{name_emp} = {empid} you were fired")
#
# deleteEmp()


# def pipeline2():
#     pipeline = [
#         {
#             '$sort': {'sal': 1}
#         }, {
#             '$project': {'ename': 1, 'sal': 1, '_id': 0}
#
#         }
#     ]
#     res = emp.aggregate(pipeline)
#     for e in res:
#         print(e)
#
#
# pipeline2()
#


def pipeline3():
    pipeline = [
        {
            '$addField':
                {
                    'commission': {'$ifNull': ['$comm', 0]}
                }
        },
        {
            '$addFields':
                {
                    'totalSalary': {'$add': ['$sal', '$commission']}
                }
        },
        {
            '$project': {'ename': 1, 'commission': 1, 'sal': 1, 'totalSalary': 1}
        }
    ]
    res = emp.aggregate(pipeline)

    for e in res:
        print(e)

pipeline3()
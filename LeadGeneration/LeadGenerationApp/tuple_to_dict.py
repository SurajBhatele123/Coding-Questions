def parsetodictAll(cursor):
    records=cursor.fetchall()
    description=cursor.description
    columnsnames=[]
    for des in description :
        columnsnames.append(des[0])
    data=[]
    for row  in records :
        data.append(dict(zip(columnsnames,list(row))))
    print("Data",data)
    return data

# for one columnsnames

def parsetodictone(cursor):
    records=cursor.fetchone()
    description=cursor.description
    columnsnames=[]
    for des in description :
        columnsnames.append(des[0])
    data=[]
    data=dict(zip(columnsnames,list(records)))
    print("Data",data)
    return data


# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import sys, os, sqlite3


FilesDB = sqlite3.connect("FileData.db")


def ripper(directory):
    DirectoryListing = sorted(os.listdir("G:\LEVELS\PWADS"))
    DirectoryListing = ["G:\LEVELS\PWADS\\" + s for s in DirectoryListing]
    return DirectoryListing

def addlistings(Type, List):
    if Type == "MAP":
        cursor = FilesDB.cursor()
        Query = """INSERT INTO MAPS (ID, PATH, NAME, DESCRIPTION, RATING) VALUES (?,?,?,?,?);"""
        DataToInsert = []
        for id, x in enumerate(List):
            head, tail = os.path.split(List[id])
            DataToInsert.append((List[id],head,tail, "",3))
            #print(DataToInsert)
        cursor.executemany(Query, DataToInsert)
        FilesDB.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into MAPS table")
        FilesDB.commit()
        cursor.close()

#FilesDB.execute('''CREATE TABLE MAPS
#             (ID INT PRIMARY KEY     NOT NULL,
#             PATH           TEXT    NOT NULL,
#             NAME           TEXT     NOT NULL,
#             DESCRIPTION    TEXT,
#             RATING         TEXT);''')

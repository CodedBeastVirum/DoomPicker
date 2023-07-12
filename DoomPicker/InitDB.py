# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


import sqlite3

FilesDB = sqlite3.connect("FileData.db")

FilesDB.execute('''CREATE TABLE IWADS
         (ID INT PRIMARY KEY     NOT NULL,
         PATH           TEXT    NOT NULL,
         NAME           TEXT     NOT NULL,
         DESCRIPTION    TEXT,
         RATING         TEXT);''')

FilesDB.execute('''CREATE TABLE MODS
         (ID INT PRIMARY KEY     NOT NULL,
         PATH           TEXT    NOT NULL,
         NAME           TEXT     NOT NULL,
         DESCRIPTION    TEXT,
         RATING         TEXT);''')


FilesDB.execute('''CREATE TABLE MAPS
         (ID INT PRIMARY KEY     NOT NULL,
         PATH           TEXT    NOT NULL,
         NAME           TEXT     NOT NULL,
         DESCRIPTION    TEXT,
         RATING         TEXT);''')


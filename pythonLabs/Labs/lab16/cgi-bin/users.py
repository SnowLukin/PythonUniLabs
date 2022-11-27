#!/usr/bin/env python3
import cgi
import cgitb
import sqlite3 as lite
import html
import bd_handler

form = cgi.FieldStorage()

create_check_flag = form.getfirst("new_submit", "")
edit_check_flag = form.getfirst("edit_submit", "")
cgitb.enable()

print("""
<html>
    <head>
        <link type="text/css" rel="stylesheet" href="/posts_styles.css">
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="60">
        <script type="text/javascript">
            function deleteFlag(index) {
                document.getElementById(index.toString()).value = "flag";
            }

            function createFlag() {
                document.getElementById("new_submit").value = "flag";
            }

            function createFlag() {
                document.getElementById("new_submit").value = "flag";
            }

            function editFlag() {
                document.getElementById("edit_submit").value = "flag";
            }
        </script>
    </head>
    <body>
""")
print("""
<div class="header">
    <h1>Chefs</h1>
    <button class="headerButton" onclick="window.location.replace('http://localhost:8000');">Go Back</button>
</div>
""")

con = lite.connect('ProChef_DataBase.db')

areaList = []

if create_check_flag == "flag":
    name = form.getfirst("new_name", "")
    surname = form.getfirst("new_surname", "")

    name = html.escape(name)
    surname = html.escape(surname)

    bd_handler.create_user(name, surname)

if edit_check_flag == "flag":
    edit_id = form.getfirst("edit_id", "")
    edit_name = form.getfirst("edit_name", "")
    edit_surname = form.getfirst("edit_surname", "")

    edit_id = html.escape(edit_id)
    edit_name = html.escape(edit_name)
    edit_surname = html.escape(edit_surname)

    if edit_id.isnumeric():
        bd_handler.edit_user(int(edit_id), edit_name, edit_surname)

with con:
    cur = con.cursor()
    sqlCommand = "select id, name, surname from Users;"
    cur.execute(sqlCommand)
    while True:
        row = cur.fetchone()
        if row is None:
            break
        areaList.append((str(row[0]), str(row[1]), str(row[2])))

print('<div class="parentPostDiv">')
for area in areaList:
    current_id = area[0]
    current_name = area[1]
    current_surname = area[2]

    delete_check_flag = form.getfirst("{}".format(current_id), "")
    if delete_check_flag == 'flag':
        areaList.remove(area)
        bd_handler.remove_user(current_id)
        continue

    # TODO: Fix alignment, remove multiple divs
    print("""
        <div class="postDiv">
            <div style="display: flex; justify-content: space-around">
                <h2>{}</h2>
                <div></div><div></div><div></div><div></div>
                <div></div><div></div><div></div><div></div>
                <div></div><div></div><div></div><div></div>
                <form action="" method=post onsubmit="deleteFlag({})">
                    <input id="{}" type="hidden" name="{}" value="">
                    <input class="deleteSubmit" type="submit" value="Delete">
                </form>
            </div>
            <h4>{}</h4>
        </div>
    """.format(current_name, current_id, current_id, current_id, current_surname))
print('</div>')
print('<div class="parentFormDiv">')
print("""
    <div class="formDiv">
        <h2>Add Chef</h2>
        <form action="" method=post onsubmit="createFlag()">
            <label for="inputID">Name:</label>
            <input class="customInput" id="inputID" type="text" name="new_name">
            <label for="story">Surname:</label>
            <input class="customInput" id="story" type="text" name="new_surname">
            <input class="customSubmit" type="submit">
            <input id="new_submit" type="hidden" name="new_submit" value="">
        </form>
    </div>
""")
print('</div>')
print('<div class="parentFormDiv">')
print("""
    <div class="formDiv">
        <h2>Edit Chef's info</h2>
        <form action="" method=post onsubmit="editFlag()">
            <label for="inputID">User id:</label>
            <input class="customInput" id="edit_id" type="text" name="edit_id">
            <label for="inputID">New name:</label>
            <input class="customInput" id="edit_name" type="text" name="edit_name">
            <label for="edit_surname">New surname:</label>
            <input class="customInput" id="edit_surname" name="edit_surname">
            <input class="customSubmit" type="submit">
            <input id="edit_submit" type="hidden" name="edit_submit" value="">
        </form>
    </div>
""")
print('</div>')
print("</body></html>")


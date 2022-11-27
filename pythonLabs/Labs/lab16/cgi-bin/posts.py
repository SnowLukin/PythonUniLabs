#!/usr/bin/env python3
import cgi
import cgitb
import sqlite3 as lite
import html
import bd_handler

form = cgi.FieldStorage()

create_check_flag = form.getfirst("new_post_submit", "")
edit_check_flag = form.getfirst("edit_post_submit", "")
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
                document.getElementById("new_post_submit").value = "flag";
            }
            
            function createFlag() {
                document.getElementById("new_post_submit").value = "flag";
            }
            
            function editFlag() {
                document.getElementById("edit_post_submit").value = "flag";
            }
        </script>
    </head>
    <body>
""")
print("""
<div class="header">
    <h1>Posts</h1>
    <button class="headerButton" onclick="window.location.replace('http://localhost:8000');">Go Back</button>
</div>
""")

con = lite.connect('ProChef_DataBase.db')

areaList = []

if create_check_flag == "flag":
    title = form.getfirst("new_post_title", "")
    body = form.getfirst("new_post_body", "")

    title = html.escape(title)
    body = html.escape(body)

    bd_handler.create_post(title, body)

if edit_check_flag == "flag":
    edit_post_id = form.getfirst("edit_post_id", "")
    edit_post_title = form.getfirst("edit_post_title", "")
    edit_post_body = form.getfirst("edit_post_body", "")

    edit_post_id = html.escape(edit_post_id)
    edit_post_title = html.escape(edit_post_title)
    edit_post_body = html.escape(edit_post_body)

    if edit_post_id.isnumeric():
        bd_handler.edit_post(int(edit_post_id), edit_post_title, edit_post_body)


with con:
    cur = con.cursor()
    sqlCommand = "select id, title, body from Posts;"
    cur.execute(sqlCommand)
    while True:
        row = cur.fetchone()
        if row is None:
            break
        areaList.append((str(row[0]), str(row[1]), str(row[2])))

print('<div class="parentPostDiv">')
for area in areaList:
    current_id = area[0]
    current_title = area[1]
    current_body = area[2]

    delete_check_flag = form.getfirst("{}".format(current_id), "")
    if delete_check_flag == 'flag':
        areaList.remove(area)
        bd_handler.remove_post(current_id)
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
    """.format(current_title, current_id, current_id, current_id, current_body))
print('</div>')
print('<div class="parentFormDiv">')
print("""
    <div class="formDiv">
        <h2>New Post</h2>
        <form action="" method=post onsubmit="createFlag()">
            <label for="inputID">Title:</label>
            <input class="customInput" id="inputID" type="text" name="new_post_title">
            <label for="story">What you wanna share:</label>
            <textarea id="story" name="new_post_body" cols="40" rows="5"></textarea>
            <input class="customSubmit" type="submit">
            <input id="new_post_submit" type="hidden" name="new_post_submit" value="">
        </form>
    </div>
""")
print('</div>')
print('<div class="parentFormDiv">')
print("""
    <div class="formDiv">
        <h2>Edit Post</h2>
        <form action="" method=post onsubmit="editFlag()">
            <label for="inputID">Post id:</label>
            <input class="customInput" id="edit_post_id" type="text" name="edit_post_id">
            <label for="inputID">New title:</label>
            <input class="customInput" id="edit_post_title" type="text" name="edit_post_title">
            <label for="story">New note:</label>
            <textarea id="edit_post_body" name="edit_post_body" cols="40" rows="5"></textarea>
            <input class="customSubmit" type="submit">
            <input id="edit_post_submit" type="hidden" name="edit_post_submit" value="">
        </form>
    </div>
""")
print('</div>')
print("</body></html>")


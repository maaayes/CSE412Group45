import psycopg2
#Setup connection
def createConn():
	connection = psycopg2.connect(
        dbname="group45",
        user="rootUser",
        password="alphaV11",
        host="localhost",
        port="5432"
    )	
	return connection

def createTables(conn):
    commands = ( #basic sql tables
        """
        CREATE TABLE Users ( 
            userID INTEGER,
            fname VARCHAR,
            lname VARCHAR,
            email VARCHAR,
            dob DATE,
            hometown VARCHAR,
            gender VARCHAR,
            password VARCHAR,
            albumNum INTEGER,
            PRIMARY KEY (userID),
            UNIQUE (userID)
        )
        """,
        """
        CREATE TABLE Friends (
            userID INTEGER,
            friend INTEGER,
            friendshipDate DATE,
            PRIMARY KEY (userID),
            UNIQUE (userID),
            UNIQUE (friend)
        )
        """,
	  """
        CREATE TABLE Albums (
            uad INTEGER PRIMARY KEY,
            name VARCHAR,
            uid INTEGER UNIQUE,
            doc DATE
        )
        """,
        """
        CREATE TABLE Photos (
            upd INTEGER UNIQUE PRIMARY KEY,
            uad INTEGER,
            caption VARCHAR,
            data VARCHAR,
            filepath VARCHAR
        )
        """,
        """
        CREATE TABLE Likes (
            upd INTEGER PRIMARY KEY,
            userID INTEGER UNIQUE,
            likecount INTEGER
        )
        """,
        """
        CREATE TABLE Tags (
            tag VARCHAR PRIMARY KEY,
            upd INTEGER 
        )
        """,
        """
        CREATE TABLE Comments (
            ucd INTEGER PRIMARY KEY,
            text VARCHAR,
            userID INTEGER,
            upd INTEGER,
            dateleft DATE
        )
        """
    )
    #unixSocket = '/cloudsql/{}'.format("coherent-answer-384517:us-central1:group45")
                #Ignore failed attempt to use google cloud :(

    try:
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
#Rest of Functions follow similar format sql insert/select/etc then conn.cursor() navigates to it.
def insertUser(userId, fname, lname, email, dob, hometown, gender, password, albumNum,conn):
    sql = """
    INSERT INTO Users (userID, fname, lname, email, dob, hometown, gender, password, albumNum)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId, fname, lname, email, dob, hometown, gender, password, albumNum))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def selectUserById(conn, userId):
    sql = "SELECT * FROM Users WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId,))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectUserByIdAndPassword(conn, userId, password):
    sql = "SELECT * FROM Users WHERE userID = %s AND password = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId, password))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)     
def searchUsersByName(conn, name):
    sql = """
    SELECT * FROM Users
    WHERE fname ILIKE %s OR lname ILIKE %s
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (f"%{name}%", f"%{name}%"))
        results = cur.fetchall()
        for result in results:
            return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateUserAlbumcount(conn, userId, newAlbumNum):
    sql = "UPDATE Users SET albumNum = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newAlbumNum, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateUserPassword(conn, userId, newPassword):
    sql = "UPDATE Users SET password = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newPassword, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateUserGender(conn, userId, newGender):
    sql = "UPDATE Users SET gender = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newGender, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateUserHometown(conn, userId, newHometown):
    sql = "UPDATE Users SET hometown = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newHometown, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateUserDob(conn, userId, newDob):
    sql = "UPDATE Users SET dob = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newDob, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateUserEmail(conn, userId, newEmail):
    sql = "UPDATE Users SET email = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newEmail, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateUserFname(conn, userId, newFname):
    sql = "UPDATE Users SET fname = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newFname, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def updateUserLname(conn, userId, newLname):
    sql = "UPDATE Users SET lname = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (newLname, userId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)

def deleteUser(conn, userId):
    sql = "DELETE FROM Users WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insertFriend(conn, userId, friendId, friendshipDate):
    sql = """
    INSERT INTO Friends (userID, friend, friendshipDate)
    VALUES (%s, %s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (userId, friendId, friendshipDate))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectFriendsByUserId(conn, userId):
    sql = "SELECT * FROM Friends WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId,))
        results = cur.fetchall()
        return results
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectUserByEmail(conn,friendEmail):
    sql = "SELECT * FROM Users WHERE email = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (friendEmail,))
        return cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
def getAllPhotos(conn):
    cursor = conn.cursor()
    query = "SELECT upd, uad, caption, data, filepath FROM photos;"
    cursor.execute(query)
    
    photos = []
    for row in cursor.fetchall():
        photo = {
            'upd': row[0],
            'uad': row[1],
            'caption': row[2],
            'data': row[3],
            'filepath': row[4]
        }
        photos.append(photo)
    print(photos)
    return photos            
def deleteFriend(conn, userId, friendId):
    sql = "DELETE FROM Friends WHERE userID = %s AND friend = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId, friendId))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insertAlbum(conn, uad, name, uid, doc):
    sql = """
    INSERT INTO Albums (uad, name, uid, doc)
    VALUES (%s, %s, %s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (uad, name, uid, doc))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectAlbumByUad(conn, uad):
    sql = "SELECT * FROM Albums WHERE uad = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectAlbumsByUid(conn, uid):
    sql = "SELECT * FROM Albums WHERE uid = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uid,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def deleteAlbum(conn, uad):
    sql = "DELETE FROM Albums WHERE uad = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def getAllPhotosForAlbum(conn, uad):
    sql = "SELECT * FROM Photos WHERE uad = %s"

    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        results = cur.fetchall()
        return results

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertPhoto(conn, upd, uad, caption, data,filename):
    sql = """
    INSERT INTO Photos (upd, uad, caption, data, filepath)
    VALUES (%s, %s, %s, %s,%s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (upd, uad, caption, data, filename))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
# Select a photo by upd (unique photo id)
def selectPhotoByUpd(conn, upd):
    sql = "SELECT * FROM Photos WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Select all photos by uad (unique album id)
def selectPhotosByUad(conn, uad):
    sql = "SELECT * FROM Photos WHERE uad = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def deletePhoto(conn, upd):
    sql = "DELETE FROM Photos WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insertLike(conn, upd, userId, likeCount):
    sql = """
    INSERT INTO Likes (upd, userId, likeCount)
    VALUES (%s, %s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (upd, userId, likeCount))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectLikeCountByUpd(conn, upd):
    sql = "SELECT likecount FROM Likes WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        result = cur.fetchone()
        print(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Select likeCount by userId (unique user id)
def selectLikeCountByUserId(conn, userId):
    sql = "SELECT likecount FROM Likes WHERE userId = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
# Increment likeCount for a specific upd (unique photo id)
def incrementLikeCount(conn, upd):
    sql = "UPDATE Likes SET likecount = likecount + 1 WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Decrement likeCount for a specific upd (unique photo id)
def decrementLikeCount(conn, upd):
    sql = "UPDATE Likes SET likecount = GREATEST(likecount - 1, 0) WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insertTag(conn, tag, upd):
    sql = """
    INSERT INTO Tags (tag, upd)
    VALUES (%s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (tag, upd))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectTagsByUpd(conn, upd):
    sql = "SELECT tag FROM Tags WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insertComment(conn, ucd, text, userId, upd, dateleft):
    sql = """
    INSERT INTO Comments (ucd, text, userID, upd, dateleft)
    VALUES (%s, %s, %s, %s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (ucd, text, userId, upd, dateleft))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectCommentsByUserId(conn, userId):
    sql = "SELECT text FROM Comments WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectCommentsByUpd(conn, upd):
    sql = "SELECT text FROM Comments WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectCommentsByDate(conn, dateleft):
    sql = "SELECT text FROM Comments WHERE dateleft = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (dateleft,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def recommendFriends(conn, userId):
    sql = """
    SELECT DISTINCT f2.friend
    FROM Friends f1
    JOIN Friends f2 ON f1.friend = f2.userID
    WHERE f1.userID = %s AND f2.friend != %s AND f2.friend NOT IN (
        SELECT friend FROM Friends WHERE userID = %s
    )
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (userId, userId, userId))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def youMayAlsoLike(conn, photoId):
    sql = """
    SELECT DISTINCT p2.*
    FROM Tags t1
    JOIN Tags t2 ON t1.tag = t2.tag
    JOIN Photos p2 ON t2.upd = p2.upd
    WHERE t1.upd = %s AND t2.upd != %s
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (photoId, photoId))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def searchPhotosByTags(conn, tag):
    sql = """
    SELECT p.*
    FROM Photos p
    JOIN Tags t ON p.upd = t.upd
    WHERE t.tag ILIKE %s
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (f"%{tag}%",))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def searchCommentsByText(conn, text):
    sql = "SELECT * FROM Comments WHERE text ILIKE %s"

    try:
        cur = conn.cursor()
        cur.execute(sql, (f"%{text}%",))
        results = cur.fetchall()
        for result in results:
            print(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def getTopTags(conn, limit):
    sql = """
    SELECT tag, COUNT(*) as count
    FROM Tags
    GROUP BY tag
    ORDER BY count DESC
    LIMIT %s
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (limit,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def selectPhotosByUserId(conn, userId):
    sql = """
        SELECT Photos.* 
        FROM Photos
        JOIN Users ON Photos.uad = Users.uad
        WHERE Users.uad = %s
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def selectCommentsByUserId(conn, userId):
    sql = "SELECT * FROM Comments WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (userId,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
# Usage example
if __name__ == "_Main__":
    conn = createConn()
    createTables(conn)

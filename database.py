import psycopg2
def create_conn():
	connection = psycopg2.connect(
        dbname="group45",
        user="rootUser",
        password="alphaV11",
        host="localhost",
        port="5432"
    )	
	return connection

def create_tables(conn):
    commands = (
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
            upd INTEGER PRIMARY KEY,
            uad INTEGER UNIQUE,
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
            tag VARCHAR,
            upd INTEGER PRIMARY KEY UNIQUE
        )
        """,
        """
        CREATE TABLE Comments (
            ucd INTEGER PRIMARY KEY,
            text VARCHAR,
            userID INTEGER UNIQUE,
            upd INTEGER UNIQUE,
            dateleft DATE
        )
        """
    )
    unix_socket = '/cloudsql/{}'.format("coherent-answer-384517:us-central1:group45")


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
def insert_user(user_id, fname, lname, email, dob, hometown, gender, password, album_num,conn):
    sql = """
    INSERT INTO Users (userID, fname, lname, email, dob, hometown, gender, password, albumNum)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id, fname, lname, email, dob, hometown, gender, password, album_num))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def select_user_by_id(conn, user_id):
    sql = "SELECT * FROM Users WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def select_user_by_id_and_password(conn, user_id, password):
    sql = "SELECT * FROM Users WHERE userID = %s AND password = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id, password))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)     
def search_users_by_name(conn, name):
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

def update_user_albumcount(conn, user_id, new_album_num):
    sql = "UPDATE Users SET album_num = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_album_num, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_user_password(conn, user_id, new_password):
    sql = "UPDATE Users SET password = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_password, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_user_gender(conn, user_id, new_gender):
    sql = "UPDATE Users SET gender = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_gender, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_user_hometown(conn, user_id, new_hometown):
    sql = "UPDATE Users SET hometown = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_hometown, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_user_dob(conn, user_id, new_dob):
    sql = "UPDATE Users SET dob = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_dob, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_user_email(conn, user_id, new_email):
    sql = "UPDATE Users SET email = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_email, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_user_fname(conn, user_id, new_fname):
    sql = "UPDATE Users SET fname = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_fname, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def update_user_lname(conn, user_id, new_lname):
    sql = "UPDATE Users SET lname = %s WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_lname, user_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_user(conn, user_id):
    sql = "DELETE FROM Users WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insert_friend(conn, user_id, friend_id, friendship_date):
    sql = """
    INSERT INTO Friends (userID, friend, friendshipDate)
    VALUES (%s, %s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id, friend_id, friendship_date))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def select_friends_by_user_id(conn, user_id):
    sql = "SELECT * FROM Friends WHERE userID = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        results = cur.fetchall()
        return results
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def delete_friend(conn, user_id, friend_id):
    sql = "DELETE FROM Friends WHERE userID = %s AND friend = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id, friend_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insert_album(conn, uad, name, uid, doc):
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
def select_album_by_uad(conn, uad):
    sql = "SELECT * FROM Albums WHERE uad = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def select_albums_by_uid(conn, uid):
    sql = "SELECT * FROM Albums WHERE uid = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uid,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def delete_album(conn, uad):
    sql = "DELETE FROM Albums WHERE uad = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def get_all_photos_for_album(conn, uad):
    sql = "SELECT * FROM Photos WHERE uad = %s"

    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        results = cur.fetchall()
        return results

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_photo(conn, upd, uad, caption, data,filename):
    sql = """
    INSERT INTO Photos (upd, uad, caption, data,filepath)
    VALUES (%s, %s, %s, %s,%s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (upd, uad, caption, data,filepath))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
# Select a photo by upd (unique photo id)
def select_photo_by_upd(conn, upd):
    sql = "SELECT * FROM Photos WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        result = cur.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Select all photos by uad (unique album id)
def select_photos_by_uad(conn, uad):
    sql = "SELECT * FROM Photos WHERE uad = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (uad,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def delete_photo(conn, upd):
    sql = "DELETE FROM Photos WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insert_like(conn, upd, user_id, like_count):
    sql = """
    INSERT INTO Likes (upd, user_id, like_count)
    VALUES (%s, %s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (upd, user_id, like_count))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def select_like_count_by_upd(conn, upd):
    sql = "SELECT like_count FROM Likes WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        result = cur.fetchone()
        print(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Select like_count by user_id (unique user id)
def select_like_count_by_user_id(conn, user_id):
    sql = "SELECT like_count FROM Likes WHERE user_id = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
# Increment like_count for a specific upd (unique photo id)
def increment_like_count(conn, upd):
    sql = "UPDATE Likes SET like_count = like_count + 1 WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Decrement like_count for a specific upd (unique photo id)
def decrement_like_count(conn, upd):
    sql = "UPDATE Likes SET like_count = GREATEST(like_count - 1, 0) WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insert_tag(conn, tag, upd):
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
def select_tags_by_upd(conn, upd):
    sql = "SELECT tag FROM Tags WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        results = cur.fetchall()
        for result in results:
            print(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def insert_comment(conn, ucd, text, user_id, upd, dateleft):
    sql = """
    INSERT INTO Comments (ucd, text, user_id, upd, dateleft)
    VALUES (%s, %s, %s, %s, %s)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (ucd, text, user_id, upd, dateleft))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def select_comments_by_user_id(conn, user_id):
    sql = "SELECT ucd FROM Comments WHERE user_id = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def select_comments_by_upd(conn, upd):
    sql = "SELECT ucd FROM Comments WHERE upd = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (upd,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def select_comments_by_date(conn, dateleft):
    sql = "SELECT ucd FROM Comments WHERE dateleft = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (dateleft,))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def recommend_friends(conn, user_id):
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
        cur.execute(sql, (user_id, user_id, user_id))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def you_may_also_like(conn, photo_id):
    sql = """
    SELECT DISTINCT p2.*
    FROM Tags t1
    JOIN Tags t2 ON t1.tag = t2.tag
    JOIN Photos p2 ON t2.upd = p2.upd
    WHERE t1.upd = %s AND t2.upd != %s
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (photo_id, photo_id))
        results = cur.fetchall()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def search_photos_by_tags(conn, tag):
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
def search_comments_by_text(conn, text):
    sql = "SELECT * FROM Comments WHERE text ILIKE %s"

    try:
        cur = conn.cursor()
        cur.execute(sql, (f"%{text}%",))
        results = cur.fetchall()
        for result in results:
            print(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def get_top_tags(conn, limit):
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

# Usage example
if __name__ == "__main__":
    conn = create_conn()
    create_tables(conn)

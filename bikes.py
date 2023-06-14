import sqlite3 #importing sqlite3 module

db = sqlite3.connect('bikes.db') #connecting to database
db.isolation_level = None


def distance_of_user(user: str): #getting distance sum of user from database
    sql = db.execute('''
                        SELECT SUM(T.distance) 
                        FROM Users U
                            LEFT JOIN Trips T ON U.id = T.user_id
                        WHERE U.name = ?
                    '''
                    , [user]
                    ).fetchone()[0]

    return sql



def speed_of_user(user: str):
    distance_sum = distance_of_user(user) #getting distance sum of user from database

    #getting duration sum of user from database
    duration_sum = db.execute('''
                                SELECT SUM(T.duration)
                                FROM Trips T
                                LEFT JOIN Users U ON T.user_id = U.id
                                WHERE U.name = ?
                            '''
                            , [user]
                            ).fetchone()[0]


    avg_speed = (distance_sum / 1000) / (duration_sum / 60) #calculating average speed of user in km/h

    return round(avg_speed, 2) #returning average speed of user in km/h and rounding it to 2 decimal places



def duration_in_each_city(day: str): #getting duration sum of each city on a specific day from database
    sql = db.execute('''
                    SELECT C.name, SUM(T.duration)
                    FROM Trips T
                        LEFT JOIN Bikes B ON T.bike_id = B.id
                        LEFT JOIN Cities C ON B.city_id = C.id
                    WHERE T.day = ?
                    GROUP BY C.name
                    '''
                    , [day]
                    ).fetchall()
                    
    return sql


def users_in_city(city: str): #getting users in a specific city from database
    sql = db.execute('''
                    SELECT COUNT(DISTINCT T.user_id)
                    FROM Trips T
                        LEFT JOIN Bikes B ON T.bike_id = B.id
                        LEFT JOIN Cities C ON B.city_id = C.id
                    WHERE C.name = ?
                     '''
                    , [city] 
                    ).fetchone()[0]
                
    return sql


def trips_on_each_day(city: str): #getting trips on each day in a specific city from database
    sql = db.execute('''
                    SELECT T.day, COUNT(T.user_id)
                    FROM Trips T
                        LEFT JOIN Bikes B ON T.bike_id = B.id
                        LEFT JOIN Cities C ON B.city_id = C.id
                    WHERE C.name = ?
                    GROUP BY T.day
                     '''
                    , [city] 
                    ).fetchall()
                
    return sql


def most_popular_start(city: str): #getting most popular start station and number of trips from database
    sql = db.execute('''
                    SELECT S.name, COUNT(T.from_id) 
                    FROM Trips T
                        LEFT JOIN Bikes B ON T.bike_id = B.id
                        LEFT JOIN Cities C ON B.city_id = C.id
                        LEFT JOIN Stops S ON S.id= T.from_id
                    WHERE C.name = ?
                    GROUP BY S.name 
                    ORDER BY COUNT(T.from_id) DESC LIMIT 1
                     '''
                    , [city] 
                    ).fetchone()
                
    return sql
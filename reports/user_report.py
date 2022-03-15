class UserReport:
  def __init__(self, database_cursor):
    self.cur = database_cursor
  
  def process(self):
    #self.cur.execute("SELECT COUNT(1) FROM users")
    self.cur.execute("""SELECT     users.username, 
                                   users.id                   AS user_id, 
                                   Count(DISTINCT(albums.id)) AS number_of_albums, 
                                   Count(DISTINCT(todos.id))  AS remaining_todos 
                        FROM       users users 
                        LEFT JOIN  albums albums 
                        ON         users.id = albums.userid 
                        CROSS JOIN todos todos 
                        ON         users.id = todos.userid 
                        WHERE      todos.completed IS false 
                        GROUP BY   users.id 
                        ORDER BY   number_of_albums DESC, 
                                   remaining_todos ASC"""
    )
    return self.cur.fetchall()

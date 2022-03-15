class UserReport:
  def __init__(self, database_cursor):
    self.cur = database_cursor
  
  def process(self):
    self.cur.execute("SELECT COUNT(1) FROM users")
    return self.cur.fetchone()[0]

import pytest
import database
import migrations
import load_data
import reports.user_report
import pandas as pd

# Fixture for a test databse connection
@pytest.fixture(autouse=False)
def connection():
    db_name = 'test'
    connection = database.get_connection(db_name)
    migrations.migrate(connection)
    load_data.load(db_name)
    yield connection
    database.delete_db(db_name)

def test_user_report(connection):
  # Run the report
  ur = reports.user_report.UserReport(connection.cursor())
  data = ur.process()
  df = pd.DataFrame(data)

  # We should have 4 users from the initial population
  assert len(data) == 4
  assert type(data) == list
  assert type(data[0]) == tuple
  # Each records should have 4 columns
  assert len(data[0]) == 4
  # Checking data type
  assert type(data[0][0]) == str
  assert type(data[0][1]) == int
  assert type(data[0][2]) == int
  assert type(data[0][3]) == int
  # Checking for duplicates
  assert df[df.duplicated()].empty == True
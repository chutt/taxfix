import database
import reports.user_report

connection = database.get_connection()
cur = connection.cursor()

# User count report
user_report = reports.user_report.UserReport(cur)
user_report_data = user_report.process()
print(f'We have {user_report_data} users')
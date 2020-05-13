import os
# host = "52.255.162.235"
# user = "wordpress"
# passwd = "wordpress"
# token = "1221686129:AAE5LMMmpaOJUkf-JR8TTiXvSMJDM1bxrmM"
host = os.environ['DB_HOST']
user = os.environ['DB_USER']
# passwd = ""
passwd = os.environ['DB_PASSWORD']
#token = "1221686129:AAE5LMMmpaOJUkf-JR8TTiXvSMJDM1bxrmM"
token = os.environ['TELEGRAM_TOKEN']

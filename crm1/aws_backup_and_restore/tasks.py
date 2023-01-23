from sh import pg_dump
import os, boto3, psycopg2, pexpect
from datetime import datetime
from celery import shared_task


bucket_name = 'demo-1-d2023-jan-18'
file_name = 'demo_1_y2023mjand21h20m31s06.sql'
new_db_name = 'demo_1_y2023mjand21h20m31s06'

@shared_task(bind=True)
def backup_aws_func(self,):
  '''it will back up database to aws s3'''
  print("fetching database...")
  date_time = datetime.now().strftime("y%Ym%bd%dh%Hm%Ms%S%z")
  file_name = f"demo_1_{date_time}.sql".lower()
  print(file_name)

  # download db from rds
  pg_dump(host='database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com', username='awspostgres', dbname='demo_1', file=file_name)

  print("saving database...")
  # upload db to s3
  s3_resource = boto3.resource('s3')

  bucket_name = 'demo-1-d2023-jan-18'

  s3_resource.meta.client.upload_file(
      Filename=file_name, 
      Bucket=bucket_name,
      Key=file_name
    )

  # delete dowloaded db local

  os.remove(file_name) 
  print("done backup.")
  
  # add log to map by bucket 
  
  
def get_db_from_s3():
  '''download database from s3'''
  print("fetching database...")
  s3_resource = boto3.resource('s3')

  s3_resource.Object(bucket_name, file_name).download_file(f'{file_name}')

# 

def create_new_db():
  '''create new db for restoring'''
  print("creating database")
  #establishing the connection
  conn = psycopg2.connect(
  database="demo_1", user='awspostgres', password='q8m^.mRR', host='database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com', port= '5432'
  )
  conn.autocommit = True

  #Creating a cursor object using the cursor() method
  cursor = conn.cursor()

  #Preparing query to create a database
  sql = f'''CREATE database {new_db_name}''';

  #Creating a database
  cursor.execute(sql)
  print("Database created successfully........")

  #Closing the connection
  conn.close()

def restore_db():
  print("restoring database...")
  try:
    child = pexpect.spawn(f'psql -h database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com -U awspostgres -d {new_db_name} -f {file_name}')
    child.expect('.*Password:*')
    child.sendline('q8m^.mRR')
    child.expect(pexpect.EOF)
    print(child.before)
  
  except:
    print("Exception was thrown")
    print("debug information:")
    print(str(child))
      
  print("Restore Complete")
  
def replace_db_to_restored_db():
  # add this function to edit settings.py
  pass


@shared_task(bind=True)
def restore_from_backup(self,):
  # add function to select bucket and db to restore
  get_db_from_s3()
  create_new_db()
  restore_db()
  
  
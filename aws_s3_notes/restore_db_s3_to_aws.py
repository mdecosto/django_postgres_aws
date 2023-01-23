from sh import pg_restore, psql
import psycopg2, pexpect, boto3


bucket_name = 'demo-1-d2023-jan-18'
file_name = 'demo_1_y2023mjand21h18m12s20.sql'
new_db_name = 'demo_1_y2023mjand21h18m12s20'

### need to manually run by choosing the exact file to copy from s3


def get_db_from_s3():
    # download database from s3
    print("fetching database...")
    s3_resource = boto3.resource('s3')

    s3_resource.Object(bucket_name, file_name).download_file(f'{file_name}')


# dcreate new db

def create_new_db():
    print("creating database")
    #establishing the connection
    conn = psycopg2.connect(
        database="demo_1", 
        user='awspostgres', 
        password='q8m^.mRR', 
        host='database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com', 
        port= '5432'
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

# restore
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
    


get_db_from_s3()
create_new_db()
restore_db()
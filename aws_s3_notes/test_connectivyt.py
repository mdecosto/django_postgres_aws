import psycopg2

def postgres_test():
  try:
    conn = psycopg2.connect("dbname='demo_1' user='awspostgres' host='database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com' password='q8m^.mRR'")
    conn.close()
    return True
  except:
    return False


print(postgres_test())
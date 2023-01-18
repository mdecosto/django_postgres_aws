from sh import pg_dump

pg_dump(host='database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com', username='awspostgres', dbname='demo_1', file="demo_1.sql")
  
  
# sample: pg_dump -h database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com -U awspostgres -f /tmp/demo_1.sql demo_1
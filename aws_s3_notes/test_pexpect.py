import pexpect
# pg_dump -h database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com -U awspostgres -f test.sql demo_1
try:
  child = pexpect.spawn('psql -h database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com -U awspostgres -d new_demo_1 -f demo_1-D2023-Jan-18T12-42-27.sql')
  # child = pexpect.spawn('pg_dump -h database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com -U awspostgres -f test.sql demo_1')
  child.expect('.*Password:*')
  child.sendline('q8m^.mRR')
  child.expect(pexpect.EOF)
  print(child.before)
  
  # child.wait()
except:
    print("Exception was thrown")
    print("debug information:")
    print(str(child))
    print(123)
    
    # Password for user awspostgres: 
print("done")
    
# pg_restore -h database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com -f test.sql > new_demo_1
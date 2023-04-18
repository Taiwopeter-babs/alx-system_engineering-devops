-- configure replication on replica server
CHANGE master TO
master_host='18.235.234.96',
master_user='replica_user',
master_password='projectcorrection280hbtn',
master_log_file='mysql-bin.000001',
master_log_pos=154;

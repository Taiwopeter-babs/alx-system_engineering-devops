-- configure replication on replica server
CHANGE REPLICATION SOURCE TO
SOURCE_HOST='18.235.234.96',
SOURCE_USER='replica_user',
SOURCE_PASSWORD='projectcorrection280hbtn',
SOURCE_LOG_FILE='mysql-bin.000001',
SOURCE_LOG_POS=154;

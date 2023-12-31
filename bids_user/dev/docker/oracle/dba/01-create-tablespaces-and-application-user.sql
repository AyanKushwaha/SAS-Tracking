-- create tablespace cp_sas
CREATE SMALLFILE TABLESPACE cp_sas
DATAFILE
  'cp_sas' SIZE 10M AUTOEXTEND ON NEXT 10M
LOGGING
DEFAULT NOCOMPRESS
  ONLINE
EXTENT MANAGEMENT LOCAL AUTOALLOCATE
SEGMENT SPACE MANAGEMENT AUTO;

-- create user cp_sas
CREATE USER cp_sas
IDENTIFIED BY cp_sas
DEFAULT TABLESPACE cp_sas TEMPORARY TABLESPACE TEMP;

-- grand all required to cp_sas
GRANT SELECT ON sys.dba_pending_transactions TO cp_sas;
GRANT SELECT ON sys.pending_trans$ TO cp_sas;
GRANT SELECT ON sys.dba_2pc_pending TO cp_sas;
GRANT EXECUTE ON sys.dbms_system TO cp_sas;
GRANT CONNECT TO cp_sas;
GRANT RESOURCE TO cp_sas;
GRANT CREATE VIEW TO cp_sas;
GRANT CREATE PUBLIC SYNONYM TO cp_sas;
ALTER USER cp_sas DEFAULT ROLE ALL;

-- commit changes
COMMIT;

-- exit
EXIT;

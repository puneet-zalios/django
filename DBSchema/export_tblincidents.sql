--------------------------------------------------------
--  File created - Wednesday-October-28-2020   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table TBL_INCIDENTS
--------------------------------------------------------

  CREATE TABLE "FUSION"."TBL_INCIDENTS" 
   (	"INCIDENTID" VARCHAR2(128 CHAR), 
	"UPDATEDDATE" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"UPDATEDBY" VARCHAR2(256 CHAR), 
	"CREATEDDATE" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"CREATEDBY" VARCHAR2(256 CHAR), 
	"CPID" VARCHAR2(128 CHAR), 
	"CURRENTSTATUS" VARCHAR2(96 CHAR), 
	"STARTDATE" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"ENDDATE" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"INCACTIVITYID" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"LATESTACTIVITYID" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"CREATEDORG" VARCHAR2(128 CHAR), 
	"UPDATEDORG" VARCHAR2(128 CHAR), 
	"CHANNEL" VARCHAR2(32 CHAR), 
	"ORGANIZATIONID" VARCHAR2(32 CHAR), 
	"EXPIRYDATE" TIMESTAMP (6)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" 
  PARALLEL 4 ;
--------------------------------------------------------
--  DDL for Index IDX_INC_UPD_ST
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INC_UPD_ST" ON "FUSION"."TBL_INCIDENTS" ("UPDATEDDATE", "CURRENTSTATUS", "INCIDENTID", "INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCS_ORG
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCS_ORG" ON "FUSION"."TBL_INCIDENTS" ("ORGANIZATIONID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCID_CREATEDDATE
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCID_CREATEDDATE" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "CREATEDDATE") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INC_CREATEDDATE
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INC_CREATEDDATE" ON "FUSION"."TBL_INCIDENTS" ("CREATEDDATE") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCS_LIAST
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCS_LIAST" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "LATESTACTIVITYID", "CURRENTSTATUS") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_UDATE_INCS
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_UDATE_INCS" ON "FUSION"."TBL_INCIDENTS" ("UPDATEDDATE", "INCIDENTID", "INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_ORGID
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_ORGID" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "INCACTIVITYID", "ORGANIZATIONID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INC_UPDATEDDATE
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INC_UPDATEDDATE" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "UPDATEDDATE") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_CURRENTSTATUS
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_CURRENTSTATUS" ON "FUSION"."TBL_INCIDENTS" ("UPDATEDDATE", "CURRENTSTATUS") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index PK_INCIDENTS
--------------------------------------------------------

  CREATE UNIQUE INDEX "FUSION"."PK_INCIDENTS" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_INCACTID_ST
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_INCACTID_ST" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "INCACTIVITYID", "CURRENTSTATUS") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_INCACTID_INDEX
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_INCACTID_INDEX" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_ACTID
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_ACTID" ON "FUSION"."TBL_INCIDENTS" ("INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_CURSTATUS
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_CURSTATUS" ON "FUSION"."TBL_INCIDENTS" ("CURRENTSTATUS") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCS_UDT_ST
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCS_UDT_ST" ON "FUSION"."TBL_INCIDENTS" ("INCACTIVITYID", "UPDATEDDATE", "INCIDENTID", UPPER("CURRENTSTATUS"), TO_CHAR("UPDATEDDATE",'YYYY-MM-DD')) 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCS_UDT_USTAT
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCS_UDT_USTAT" ON "FUSION"."TBL_INCIDENTS" ("UPDATEDDATE", UPPER("CURRENTSTATUS"), "INCIDENTID", "INCACTIVITYID", TO_CHAR("UPDATEDDATE",'YYYY-MM-DD')) 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX$$_00010003
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX$$_00010003" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "LATESTACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCS_LA_UP
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCS_LA_UP" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "INCACTIVITYID", "LATESTACTIVITYID", "UPDATEDDATE") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_CURSTATUS_3
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_CURSTATUS_3" ON "FUSION"."TBL_INCIDENTS" (UPPER("CURRENTSTATUS")) 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_CURSTATUS_2
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_CURSTATUS_2" ON "FUSION"."TBL_INCIDENTS" (UPPER("CURRENTSTATUS"), "INCIDENTID", "INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCIDENTS_CURSTATUS_4
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCIDENTS_CURSTATUS_4" ON "FUSION"."TBL_INCIDENTS" (UPPER("CURRENTSTATUS"), "CHANNEL", "INCIDENTID", "INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  Constraints for Table TBL_INCIDENTS
--------------------------------------------------------

  ALTER TABLE "FUSION"."TBL_INCIDENTS" MODIFY ("INCIDENTID" NOT NULL ENABLE);
  ALTER TABLE "FUSION"."TBL_INCIDENTS" ADD SUPPLEMENTAL LOG DATA (UNIQUE INDEX) COLUMNS;
  ALTER TABLE "FUSION"."TBL_INCIDENTS" ADD SUPPLEMENTAL LOG DATA (FOREIGN KEY) COLUMNS;
  ALTER TABLE "FUSION"."TBL_INCIDENTS" ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY) COLUMNS;
  ALTER TABLE "FUSION"."TBL_INCIDENTS" ADD CONSTRAINT "PK_INCIDENTS" PRIMARY KEY ("INCIDENTID")
  USING INDEX (CREATE INDEX "FUSION"."IDX_INCIDENTS_INCACTID_INDEX" ON "FUSION"."TBL_INCIDENTS" ("INCIDENTID", "INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" )  ENABLE;
  ALTER TABLE "FUSION"."TBL_INCIDENTS" ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
--------------------------------------------------------
--  DDL for Trigger TR_INCIDENTS_UPDATE
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "FUSION"."TR_INCIDENTS_UPDATE" FOR
    UPDATE OR INSERT ON tbl_incidents
COMPOUND TRIGGER
    TYPE id_primary_id IS RECORD ( incidentid         tbl_incactivity.incidentid%TYPE,
    incactivityid      tbl_incactivity.incactivityid%TYPE );
    TYPE row_level_info_t IS
        TABLE OF id_primary_id INDEX BY PLS_INTEGER;
    g_row_level_info   row_level_info_t;
    itr                INTEGER;
    indx               INTEGER;
    payload_clob       CLOB;
    inc_count          NUMBER := 0;
    err_code           VARCHAR2(20);
    err_msg            VARCHAR2(200);
    payloadid          VARCHAR2(32);
    payloadid2         VARCHAR2(32);
    AFTER EACH ROW IS BEGIN
        itr := g_row_level_info.count + 1;
        g_row_level_info(itr).incidentid :=:new.incidentid;
        g_row_level_info(itr).incactivityid :=:new.incactivityid;
    END AFTER EACH ROW;
    AFTER STATEMENT IS
        p_numaffected   NUMBER;
    BEGIN
        indx := 1;
        dbms_output.put_line('begin '
        || itr);
        FOR indx IN 1..itr LOOP
            dbms_output.put_line('inside loop '
            || itr);
            IF
                g_row_level_info(indx).incactivityid IS NOT NULL AND g_row_level_info(indx).incidentid IS NOT NULL and ((cast(systimestamp as date) - cast(g_row_level_info(indx).incactivityid as date))* 24 * 60) < 1
            THEN
                BEGIN
                    SELECT
                        COUNT(1)
                    INTO
                        inc_count
                    FROM
                        tbl_incactivity
                    WHERE
                        incidentid = g_row_level_info(indx).incidentid
                        AND   incactivityid = g_row_level_info(indx).incactivityid
                        AND   ROWNUM = 1;

                    IF
                        inc_count > 0
                    THEN
                        payload_clob := fusion.incident_json.incident_tojson(g_row_level_info(indx).incidentid,g_row_level_info(indx).incactivityid);

                        IF
                            payload_clob IS NOT NULL
                        THEN
                            INSERT INTO fusion_warehouse.tbl_azure_storage_queue (
                                storage_type,
                                payload_pk1,
                                payload_container_name,
                                payload_object,
                                payload_object_name,
                                payload_clob
                            )
                                SELECT
                                    'DOCUMENT',
                                    g_row_level_info(indx).incidentid,
                                    azure_storage_mgr.get_container_name('incactivity_collection'),
                                    'INCIDENT',
                                    'incident_document',
                                    payload_clob
                                FROM
                                    tbl_incidents
                                WHERE
                                    incidentid = g_row_level_info(indx).incidentid
                                    AND   incactivityid = g_row_level_info(indx).incactivityid;

                        END IF;

                    END IF;

                EXCEPTION
                    WHEN OTHERS THEN
                        err_code := sqlcode;
                        err_msg := substr(sqlerrm,1,200);
                        payloadid := g_row_level_info(indx).incidentid;
                        payloadid2 := g_row_level_info(indx).incactivityid;
                        INSERT INTO fusion_warehouse.tbl_azure_error (
                            error_code,
                            error_message,
                            payload_pk1,
                            payload_pk2,
                            source
                        ) VALUES (
                            err_code,
                            err_msg,
                            payloadid,
                            payloadid2,
                            'TR_INCIDENTS_UPDATE AFTER STATEMENT'
                        );

                END;

            END IF;

        END LOOP;

    EXCEPTION
        WHEN OTHERS THEN
            err_code := sqlcode;
            err_msg := substr(sqlerrm,1,200);
            dbms_output.put_line(err_code
            || ' '
            || err_msg);
    END AFTER STATEMENT;
END;
/
ALTER TRIGGER "FUSION"."TR_INCIDENTS_UPDATE" DISABLE;
--------------------------------------------------------
--  DDL for Trigger TRDT_TBL_INCIDENTS
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "FUSION"."TRDT_TBL_INCIDENTS" before insert or update on TBL_INCIDENTS for each row begin  if trgdt_mgr.isdisabled = 0 then  if inserting then :new.createddate := systimestamp; :new.createdby := context_mgr.get_fullname;  :new.createdorg := context_mgr.get_orgname;  :new.updateddate := systimestamp; :new.updatedby := context_mgr.get_fullname; :new.updatedorg := context_mgr.get_orgname;  end if; if updating then :new.updateddate := systimestamp; :new.updatedby := context_mgr.get_fullname;  :new.updatedorg := context_mgr.get_orgname; end if; end if;  end; 









/
ALTER TRIGGER "FUSION"."TRDT_TBL_INCIDENTS" ENABLE;

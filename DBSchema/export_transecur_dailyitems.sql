--------------------------------------------------------
--  File created - Thursday-October-29-2020   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table DAILYITEMS
--------------------------------------------------------

  CREATE TABLE "TRANSECUR"."DAILYITEMS" 
   (	"ITEMID" NUMBER(10,0), 
	"ITEMDATE" DATE, 
	"ITEMCOUNTRYLINE" VARCHAR2(1024 BYTE), 
	"ITEMTITLE" VARCHAR2(150 CHAR), 
	"ITEMSUMMARY" VARCHAR2(1000 CHAR), 
	"ITEMTEXT" CLOB, 
	"ITEMORDINAL" VARCHAR2(4 CHAR), 
	"ITEMCODED" NUMBER(1,0), 
	"ITEMBLURB" VARCHAR2(200 BYTE), 
	"PRIMARY_ID" VARCHAR2(32 CHAR) DEFAULT SYS_GUID(), 
	"ITEMATTRIBUTETOACTOR" VARCHAR2(1000 CHAR), 
	"ITEMCATEGORY" VARCHAR2(1024 BYTE), 
	"ITEMDISPLAYACTORINFO" VARCHAR2(4000 CHAR), 
	"ITEMEVENT" VARCHAR2(1000 CHAR), 
	"ITEMATTACHMENTLIST" CLOB, 
	"ITEMSIGNIFICANCE" VARCHAR2(150 CHAR), 
	"ITEMSTATUS" VARCHAR2(150 CHAR), 
	"ITEMUPDATEDDATE" TIMESTAMP (6), 
	"DUMMY" VARCHAR2(1 CHAR), 
	"ITEMASSESSMENT" CLOB, 
	"ITEMSTATUSCODE" NUMBER(2,0), 
	"ITEMDISPLAYACTORSLIST" VARCHAR2(2000 CHAR), 
	"CREATEDDATE" TIMESTAMP (6), 
	"CREATEDBY" VARCHAR2(128 CHAR), 
	"UPDATEDDATE" TIMESTAMP (6), 
	"UPDATEDBY" VARCHAR2(128 CHAR), 
	"OLDITEMCOUNTRYLINE" VARCHAR2(512 CHAR), 
	"ITEMEXPIRATIONDATE" TIMESTAMP (6), 
	"PUBLISHDATE" DATE, 
	"SYNOPSIS" VARCHAR2(400 CHAR), 
	"CITY" VARCHAR2(64 BYTE), 
	"COUNTRY" VARCHAR2(64 BYTE), 
	"COUNTY" VARCHAR2(128 BYTE), 
	"DISTRICT" VARCHAR2(128 BYTE), 
	"LATITUDE" FLOAT(126) DEFAULT 0.000000, 
	"LONGITUDE" FLOAT(126) DEFAULT 0.000000, 
	"POSTAL" VARCHAR2(32 BYTE), 
	"REGION" VARCHAR2(64 BYTE), 
	"STATEPROVINCE" VARCHAR2(64 BYTE), 
	"STREET" VARCHAR2(400 BYTE), 
	"ATTACHMENTLIST" CLOB DEFAULT NULL
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" 
 LOB ("ITEMTEXT") STORE AS BASICFILE (
  TABLESPACE "FUSION" ENABLE STORAGE IN ROW CHUNK 8192 RETENTION 
  NOCACHE LOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) 
 LOB ("ITEMATTACHMENTLIST") STORE AS BASICFILE (
  TABLESPACE "FUSION" ENABLE STORAGE IN ROW CHUNK 8192 RETENTION 
  NOCACHE LOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) 
 LOB ("ITEMASSESSMENT") STORE AS BASICFILE (
  TABLESPACE "FUSION" ENABLE STORAGE IN ROW CHUNK 8192 RETENTION 
  NOCACHE LOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) 
 LOB ("ATTACHMENTLIST") STORE AS SECUREFILE (
  TABLESPACE "FUSION" ENABLE STORAGE IN ROW CHUNK 8192
  NOCACHE LOGGING  NOCOMPRESS  KEEP_DUPLICATES 
  STORAGE(INITIAL 106496 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) ;
--------------------------------------------------------
--  DDL for Index DAILYITEMS_KEYWORD_INDEX
--------------------------------------------------------

  CREATE INDEX "TRANSECUR"."DAILYITEMS_KEYWORD_INDEX" ON "TRANSECUR"."DAILYITEMS" ("DUMMY") 
   INDEXTYPE IS "CTXSYS"."CONTEXT"  PARAMETERS ('datastore tstextuser.DAILYITEMS_multi_datastore filter ctxsys.null_filter sync (on commit)');
--------------------------------------------------------
--  DDL for Index IDX_DAILYITEMS_I1001
--------------------------------------------------------

  CREATE INDEX "TRANSECUR"."IDX_DAILYITEMS_I1001" ON "TRANSECUR"."DAILYITEMS" ("ITEMDATE", "ITEMORDINAL") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index PKY_DAILYITEMS
--------------------------------------------------------

  CREATE UNIQUE INDEX "TRANSECUR"."PKY_DAILYITEMS" ON "TRANSECUR"."DAILYITEMS" ("PRIMARY_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_DAILYITEMS_DTID
--------------------------------------------------------

  CREATE INDEX "TRANSECUR"."IDX_DAILYITEMS_DTID" ON "TRANSECUR"."DAILYITEMS" ("UPDATEDDATE", "ITEMID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  Constraints for Table DAILYITEMS
--------------------------------------------------------

  ALTER TABLE "TRANSECUR"."DAILYITEMS" ADD CONSTRAINT "PKY_DAILYITEMS" PRIMARY KEY ("PRIMARY_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION"  ENABLE;
  ALTER TABLE "TRANSECUR"."DAILYITEMS" MODIFY ("ITEMCODED" NOT NULL ENABLE);
  ALTER TABLE "TRANSECUR"."DAILYITEMS" MODIFY ("ITEMDATE" NOT NULL ENABLE);
  ALTER TABLE "TRANSECUR"."DAILYITEMS" MODIFY ("ITEMID" NOT NULL ENABLE);
--------------------------------------------------------
--  DDL for Trigger TR_DAILYITEMS_UPDATE
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "TRANSECUR"."TR_DAILYITEMS_UPDATE" FOR
    UPDATE OR INSERT ON dailyitems
COMPOUND TRIGGER
    TYPE id_primary_id IS RECORD ( primary_id         dailyitems.primary_id%TYPE );
    TYPE row_level_info_t IS
        TABLE OF id_primary_id INDEX BY PLS_INTEGER;
    g_row_level_info   row_level_info_t;
    err_code           VARCHAR2(20);
    err_msg            VARCHAR2(200);
    payloadid          VARCHAR2(32);
    payloadid2         VARCHAR2(32);
    AFTER EACH ROW IS BEGIN
        g_row_level_info(g_row_level_info.count + 1).primary_id :=:new.primary_id;
    END AFTER EACH ROW;
    AFTER STATEMENT IS
        p_numaffected   NUMBER;
    BEGIN
        FOR indx IN 1..g_row_level_info.count LOOP
            BEGIN
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
                        g_row_level_info(indx).primary_id,
                        fusion.azure_storage_mgr.get_container_name('dailyitems_collection'),
                        'INTEL',
                        'intel_document',
                        fusion.incident_json.dailyitem_tojson(g_row_level_info(indx).primary_id)
                    FROM
                        transecur.dailyitems
                    WHERE
                        primary_id = g_row_level_info(indx).primary_id;

            EXCEPTION
                WHEN OTHERS THEN
                    err_code := sqlcode;
                    err_msg := substr(sqlerrm,1,200);
                    payloadid := g_row_level_info(indx).primary_id;
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
                        'TR_DAILYITEMS_UPDATE AFTER STATEMENT'
                    );

            END;
        END LOOP;
    EXCEPTION
        WHEN OTHERS THEN
            err_code := sqlcode;
            err_msg := substr(sqlerrm,1,200);
            dbms_output.put_line(err_code
            || ' '
            || err_msg);
    END AFTER STATEMENT;
END tr_dailyitems_update;
/
ALTER TRIGGER "TRANSECUR"."TR_DAILYITEMS_UPDATE" ENABLE;
--------------------------------------------------------
--  DDL for Trigger DAILYITEMS_ITEMID_TRG
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "TRANSECUR"."DAILYITEMS_ITEMID_TRG" BEFORE INSERT OR UPDATE ON DailyItems
FOR EACH ROW
DECLARE 
v_newVal NUMBER(12) := 0;
v_incval NUMBER(12) := 0;
BEGIN
  IF INSERTING AND :new.ItemID IS NULL THEN
    SELECT  DailyItems_ItemID_SEQ.NEXTVAL INTO v_newVal FROM DUAL;
    -- If this is the first time this table have been inserted into (sequence == 1)
    IF v_newVal = 1 THEN 
      --get the max indentity value from the table
      SELECT NVL(max(ItemID),0) INTO v_newVal FROM DailyItems;
      v_newVal := v_newVal + 1;
      --set the sequence to that value
      LOOP
           EXIT WHEN v_incval>=v_newVal;
           SELECT DailyItems_ItemID_SEQ.nextval INTO v_incval FROM dual;
      END LOOP;
    END IF;
    -- save this to emulate @@identity
   sqlserver_utilities.identity := v_newVal; 
   -- assign the value from the sequence to emulate the identity column
   :new.ItemID := v_newVal;
  END IF;
END;






/
ALTER TRIGGER "TRANSECUR"."DAILYITEMS_ITEMID_TRG" ENABLE;

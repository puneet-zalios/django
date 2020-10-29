--------------------------------------------------------
--  File created - Wednesday-October-28-2020   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table TBL_INCATTACHMENTS
--------------------------------------------------------

  CREATE TABLE "FUSION"."TBL_INCATTACHMENTS" 
   (	"ATTACHID" VARCHAR2(32 CHAR), 
	"CREATEDDATE" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"CREATEDBY" VARCHAR2(64 CHAR), 
	"INCIDENTID" VARCHAR2(32 CHAR), 
	"INCACTIVITYID" TIMESTAMP (6) DEFAULT SYSTIMESTAMP, 
	"COMMENTID" VARCHAR2(32 CHAR), 
	"MIMETYPE" VARCHAR2(255 CHAR), 
	"ATTACHDATA" BLOB, 
	"LINKDATA" CLOB, 
	"LABEL" VARCHAR2(128 CHAR), 
	"FILENAME" VARCHAR2(255 CHAR), 
	"CREATEDORG" VARCHAR2(128 CHAR)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" 
 LOB ("ATTACHDATA") STORE AS BASICFILE (
  TABLESPACE "FUSION" ENABLE STORAGE IN ROW CHUNK 8192 PCTVERSION 10
  NOCACHE LOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) 
 LOB ("LINKDATA") STORE AS BASICFILE (
  TABLESPACE "FUSION" ENABLE STORAGE IN ROW CHUNK 8192 PCTVERSION 10
  NOCACHE LOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) ;
--------------------------------------------------------
--  DDL for Index IDX_PK_ACTIVITY_ATTACHMENTS
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_PK_ACTIVITY_ATTACHMENTS" ON "FUSION"."TBL_INCATTACHMENTS" ("INCIDENTID", "INCACTIVITYID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index PK_TBL_INCATTACHMENTS
--------------------------------------------------------

  CREATE UNIQUE INDEX "FUSION"."PK_TBL_INCATTACHMENTS" ON "FUSION"."TBL_INCATTACHMENTS" ("ATTACHID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index IDX_INCATTACH_1
--------------------------------------------------------

  CREATE INDEX "FUSION"."IDX_INCATTACH_1" ON "FUSION"."TBL_INCATTACHMENTS" ("INCIDENTID", "INCACTIVITYID", "COMMENTID", "ATTACHID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  Constraints for Table TBL_INCATTACHMENTS
--------------------------------------------------------

  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" MODIFY ("INCIDENTID" NOT NULL ENABLE);
  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" MODIFY ("ATTACHID" NOT NULL ENABLE);
  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" ADD SUPPLEMENTAL LOG DATA (UNIQUE INDEX) COLUMNS;
  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" ADD SUPPLEMENTAL LOG DATA (FOREIGN KEY) COLUMNS;
  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY) COLUMNS;
  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" ADD CONSTRAINT "PK_TBL_INCATTACHMENTS" PRIMARY KEY ("ATTACHID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION"  ENABLE;
  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
--------------------------------------------------------
--  Ref Constraints for Table TBL_INCATTACHMENTS
--------------------------------------------------------

  ALTER TABLE "FUSION"."TBL_INCATTACHMENTS" ADD CONSTRAINT "PK_ACTIVITY_ATTACHMENTS" FOREIGN KEY ("INCIDENTID", "INCACTIVITYID")
	  REFERENCES "FUSION"."TBL_INCACTIVITY" ("INCIDENTID", "INCACTIVITYID") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  DDL for Trigger TRDT_TBL_INCATTACHMENTS
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "FUSION"."TRDT_TBL_INCATTACHMENTS" before insert or update on TBL_INCATTACHMENTS for each row begin  if trgdt_mgr.isdisabled = 0 then  if inserting then :new.createddate := systimestamp; :new.createdby := context_mgr.get_fullname;  :new.createdorg := context_mgr.get_orgname;  end if;  end if;  end; 









/
ALTER TRIGGER "FUSION"."TRDT_TBL_INCATTACHMENTS" ENABLE;
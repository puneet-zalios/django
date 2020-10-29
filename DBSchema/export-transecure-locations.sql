--------------------------------------------------------
--  File created - Thursday-October-29-2020   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table LOCATIONS
--------------------------------------------------------

  CREATE TABLE "TRANSECUR"."LOCATIONS" 
   (	"LOCATIONID" NUMBER(5,0), 
	"LOCATIONNAME" VARCHAR2(50 CHAR), 
	"LOCATIONTYPE" NUMBER(3,0), 
	"LOCATIONPARENTREGION" NUMBER(5,0), 
	"LOCATIONPARENTCOUNTRY" NUMBER(5,0), 
	"LOCATIONPARENTPROVINCE" NUMBER(5,0), 
	"LOCATIONPARENTSUBPROVINCE" NUMBER(5,0), 
	"LOCATIONADMINPOWER" NUMBER(5,0), 
	"PRIMARY_ID" VARCHAR2(32 BYTE) DEFAULT SYS_GUID(), 
	"ESAREGION" VARCHAR2(512 CHAR), 
	"ESACOUNTRY" VARCHAR2(512 CHAR), 
	"ESACOUNTRYID" NUMBER(5,0), 
	"SHOW" NUMBER(1,0), 
	"OLDLOCATIONNAME" VARCHAR2(50 CHAR), 
	"NEWLOCATIONNAME" VARCHAR2(50 CHAR), 
	"ESAREGIONID" NUMBER(5,0), 
	"LATITUDE" FLOAT(126), 
	"LONGITUDE" FLOAT(126), 
	"ISOCOUNTRYCODE" VARCHAR2(3 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  DDL for Index PKY_LOCATIONS
--------------------------------------------------------

  CREATE UNIQUE INDEX "TRANSECUR"."PKY_LOCATIONS" ON "TRANSECUR"."LOCATIONS" ("PRIMARY_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION" ;
--------------------------------------------------------
--  Constraints for Table LOCATIONS
--------------------------------------------------------

  ALTER TABLE "TRANSECUR"."LOCATIONS" ADD CONSTRAINT "PKY_LOCATIONS" PRIMARY KEY ("PRIMARY_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "FUSION"  ENABLE;
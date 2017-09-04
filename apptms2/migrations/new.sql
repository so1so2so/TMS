BEGIN;
CREATE TABLE "apptms2_group"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(128) NOT NULL);
CREATE TABLE "apptms2_membership"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "date_joined" date NOT NULL,
  "invite_reason" varchar(64) NOT NULL,
  "group_id" integer NOT NULL REFERENCES "apptms2_group" ("id"));
CREATE TABLE "apptms2_person"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(128) NOT NULL);
CREATE TABLE "apptms2_membership__new"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "date_joined" date NOT NULL,
  "invite_reason" varchar(64) NOT NULL,
  "group_id" integer NOT NULL REFERENCES "apptms2_group" ("id"), "person_id" integer NOT NULL REFERENCES "apptms2_person" ("id"));
INSERT INTO "apptms2_membership__new" ("person_id", "group_id", "invite_reason", "id", "date_joined") SELECT NULL, "group_id", "invite_reason", "id", "date_joined" FROM "apptms2_membership";
DROP TABLE "apptms2_membership";
ALTER TABLE "apptms2_membership__new" RENAME TO "apptms2_membership";
CREATE INDEX "apptms2_membership_0e939a4f" ON "apptms2_membership" ("group_id");
CREATE INDEX "apptms2_membership_a8452ca7" ON "apptms2_membership" ("person_id");
CREATE TABLE "apptms2_group__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL);
INSERT INTO "apptms2_group__new" ("id", "name") SELECT "id", "name" FROM "apptms2_group";
DROP TABLE "apptms2_group";
ALTER TABLE "apptms2_group__new" RENAME TO "apptms2_group";

COMMIT;
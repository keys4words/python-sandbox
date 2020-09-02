BEGIN TRANSACTION;
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('users',5);
CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name,
        last_name,
        birthday
    );
INSERT INTO "users" VALUES(1,'Ivan','Ivanov','09-11-1985');
INSERT INTO "users" VALUES(2,'Peter','Petrov','01-02-1985');
INSERT INTO "users" VALUES(3,'Myke','Tyson','01-02-1985');
INSERT INTO "users" VALUES(4,'John','Rollings','01-02-1985');
INSERT INTO "users" VALUES(5,'Harry','Potter','01-02-1985');
COMMIT;

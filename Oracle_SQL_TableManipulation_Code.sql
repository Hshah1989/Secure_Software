/* Hiren Shah
   3/22/21
   SDEV 350 7380
   Dr. Haseltine
*/
/* Drop Table code */

Drop TABLE Engineers CASCADE CONSTRAINTS;
Drop TABLE Faculty CASCADE CONSTRAINTS;
Drop TABLE Classes CASCADE CONSTRAINTS;
Drop TABLE ClassEnrollments CASCADE CONSTRAINTS; 


CREATE TABLE Engineers (EID INT PRIMARY KEY,
                        Lastname  VARCHAR(40),
                        Firstname VARCHAR(40),
                        Email     VARCHAR(40),
                        Graddate  DATE 
                        );
                        
CREATE TABLE Faculty (FID INT PRIMARY KEY,
                       Lastname  VARCHAR(40),
                       Firstname VARCHAR(40),
                       Email     VARCHAR(40),
                       Hiredate  DATE 
                        );
                        
CREATE TABLE Classes (CID INT PRIMARY KEY,
                       Subject VARCHAR(40),
                       Catalognbr VARCHAR(40),
                       Title     VARCHAR(40)
                        );
                       
CREATE TABLE ClassEnrollments (EnID INT PRIMARY KEY, 
                               CID INT NOT NULL,
                               FID INT NOT NULL,
                               EID INT NOT NULL,
                               
                               FOREIGN KEY(CID) REFERENCES Classes(CID),
                               FOREIGN KEY(FID) REFERENCES Faculty(FID),
                               FOREIGN KEY(EID) REFERENCES Engineers(EID));
                               

/* Insert statement codes */
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (1, 'Morton', 'Harshbarger', 'MortonHarshbarger@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (2, 'Roxann', 'Engh', 'RoxannEngh@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (3, 'Gregory', 'Paez', 'GregoryPaez@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (4, 'Sage', 'Heffelfinger', 'SageHeffelfinger@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (5, 'Deidre', 'Sager', 'DeidreSager@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (6, 'Loretta', 'Suess', 'LorettaSuess@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (7, 'Lindsay', 'Lard', 'LindsayLard@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (8, 'Elfriede', 'Loder', 'ElfriedeLoder@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (9, 'Shanti', 'Isaac', 'ShantiIsaac@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (10, 'Nereida', 'Victorino', 'NereidaVictorino@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (11, 'Carman', 'Gardener', 'CarmanGardener@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (12, 'Chad', 'Roehr', 'ChadRoehr@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (13, 'Opal', 'Harrel', 'OpalHarrel@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (14, 'Chanda', 'Lamphear', 'ChandaLamphear@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));
INSERT INTO Engineers (EID, Lastname, Firstname, Email, Graddate) VALUES (15, 'Tabitha', 'Croker', 'TabithaCroker@gmail.com', TO_DATE('09/01/2021','DD-MM-YYYY'));


INSERT INTO Faculty (FID, Lastname, Firstname, Email, Hiredate) VALUES (1, 'Coralie', 'Mirelez', 'CoralieMirelez@gmail.com', TO_DATE('21/04/2019','DD-MM-YYYY'));
INSERT INTO Faculty (FID, Lastname, Firstname, Email, Hiredate) VALUES (2, 'Eleanor', 'Ackerley', 'EleanorAckerley@gmail.com', TO_DATE('22/01/2021','DD-MM-YYYY'));
INSERT INTO Faculty (FID, Lastname, Firstname, Email, Hiredate) VALUES (3, 'Leesa', 'Bertolini', 'LeesaBertolini@gmail.com', TO_DATE('23/07/2020','DD-MM-YYYY'));

INSERT INTO Classes (CID, Subject, Catalognbr, Title) VALUES (1, 'Engineering', '7 46015 2', 'Engin101');
INSERT INTO Classes (CID, Subject, Catalognbr, Title) VALUES (2, 'Mathamatics', '7 47021 3', 'Calc3');
INSERT INTO Classes (CID, Subject, Catalognbr, Title) VALUES (3, 'Biology', '7 86416 2', 'Bio350');

INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (1,1,1,1);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (2,3,3,2);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (3,2,1,3);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (4,2,1,4);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (5,3,2,5);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (6,2,3,6);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (7,3,2,7);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (8,2,1,8);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (9,3,1,9);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (10,2,2,10);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (11,2,1,11);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (12,3,1,12);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (13,1,3,13);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (14,3,1,14);
INSERT INTO ClassEnrollments (EnID, CID, FID, EID) VALUES (15,1,3,15);

/* Showing each table by descending order of primary keys */
SELECT * FROM ENGINEERS
ORDER BY EID DESC;

SELECT * FROM Faculty
ORDER BY FID DESC;

SELECT * FROM Classes
ORDER BY CID DESC;

SELECT * FROM ClassEnrollments
ORDER BY EnID DESC;

/* Updating specified tables and changing Values per assignment */
UPDATE Faculty 
SET Lastname = 'Friendship'
WHERE FID = 1;

UPDATE Engineers
SET Firstname = 'Amadeus'
WHERE EID = 1;

UPDATE Classes
SET Subject = 'IOT Cyber'
WHERE CID = 3;


DELETE FROM ClassEnrollments 
WHERE EnID = (SELECT MIN(EnID) FROM classenrollments);

SELECT E.Lastname, E.Firstname, F.Lastname, F.Email, C.Subject, C.Title
FROM ClassEnrollments CE
JOIN Engineers E
ON CE.EID = E.EID
JOIN Faculty F
ON CE.FID = F.FID
JOIN Classes C
ON CE.CID = C.CID;

SELECT CE.EnID AS EnrollmentID, E.Lastname AS Eng_Last, E.Firstname AS Eng_First, F.Lastname AS F_Last, F.Email AS F_Email, C.Subject AS Class_Subj, C.Title AS Class_title
FROM ClassEnrollments CE
JOIN Engineers E
ON CE.EID = E.EID
JOIN Faculty F
ON CE.FID = F.FID
JOIN Classes C
ON CE.CID = C.CID;

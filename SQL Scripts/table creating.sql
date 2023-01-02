CREATE TABLE `book` (
  `ISBN` varchar(13) NOT NULL DEFAULT '0',
  `ISBN10` varchar(13) DEFAULT '0',
  `title` varchar(250),
  `cover` varchar(60),
  `publisher` varchar(60),
  `page` int default '0',
  PRIMARY KEY (`ISBN`)
);

CREATE TABLE `authors` (
  `author_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(150) NOT NULL DEFAULT 'UName',
  PRIMARY KEY (`author_id`)
) ;

CREATE TABLE `book_author` (
  `isbn` varchar(13) NOT NULL DEFAULT '0',
  `author_id` int(11) NOT NULL DEFAULT '0',
  KEY `fk1_idx` (`isbn`),
  KEY `fk2_idx` (`author_id`),
  CONSTRAINT `fk1` FOREIGN KEY (`isbn`) REFERENCES `book` (`ISBN`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk2` FOREIGN KEY (`author_id`) REFERENCES `authors` (`author_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ;

CREATE TABLE `borrower` (
  `Card_Id` int(10) NOT NULL AUTO_INCREMENT,
  `Ssn` varchar(13) NOT NULL,
  `FName` varchar(100) NOT NULL DEFAULT 'Unknown_Fname',
  `LName` varchar(100) DEFAULT 'Unknown_Lname',
  `Address` varchar(150) NOT NULL DEFAULT 'Undefined_Address',
  `Phone` varchar(15) DEFAULT '(123) 456-7890',
  PRIMARY KEY (`Card_Id`,`Ssn`)
);

CREATE TABLE `book_loans` (
  `LoanID` int(10) NOT NULL AUTO_INCREMENT,
  `ISBN` varchar(13) NOT NULL DEFAULT '0',
  `Card_ID` int(10) NOT NULL DEFAULT '0',
  `Date_out` date DEFAULT NULL,
  `Due_Date` date DEFAULT NULL,
  `Date_In` date DEFAULT NULL,
  PRIMARY KEY (`LoanID`),
  UNIQUE KEY `ISBN_UNIQUE` (`ISBN`),
  KEY `fk11_idx` (`ISBN`),
  KEY `fk_cid_bl_idx` (`Card_ID`),
  CONSTRAINT `fk11` FOREIGN KEY (`ISBN`) REFERENCES `book` (`ISBN`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_cid_bl` FOREIGN KEY (`Card_ID`) REFERENCES `borrower` (`Card_Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ;

CREATE TABLE `fines` (
  `Loan_Id` int(10) NOT NULL,
  `Fine_Amt` decimal(10,2) NOT NULL DEFAULT '0.00',
  `Paid` varchar(3) DEFAULT 'No',
  -- PRIMARY KEY (`Loan_Id`),
  KEY `fk111_idx` (`Loan_Id`),
  CONSTRAINT `fk111` FOREIGN KEY (`Loan_Id`) REFERENCES `book_loans` (`LoanID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ;


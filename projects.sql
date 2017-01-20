BEGIN TRANSACTION;
CREATE TABLE `projects` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`project_name`	TEXT,
	`project_manager`	TEXT,
	`begin_date`	INTEGER,
	`deadline`	INTEGER,
	`end_date`	INTEGER,
	`comments`	TEXT
);
INSERT INTO `projects` VALUES (1,'New software update','Harry Willson',1585396800,1588334400,1588248000,'All errors was neutralized.');
INSERT INTO `projects` VALUES (2,'Behavior SDK update','John Ford',1633867200,1641816000,1640865600,'New stories already integrated.');
INSERT INTO `projects` VALUES (3,'Androids repair','Henry Kleon',1565956800,1573819200,1574251200,'New proccessors included to the android''s hardware.');
COMMIT;

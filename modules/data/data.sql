CREATE TABLE facts(
  "subject" TEXT,
  "link" TEXT,
  "goal" TEXT
);
CREATE TABLE rules(
"id" INTEGER NOT NULL PRIMARY KEY,
"premises" TEXT,
"conclusion" TEXT
);

create unique index facts_subject_link_goal on facts (subject,link,goal);
create unique index rules_premise_conclusion on rules (premises,conclusion);

-- Mój plik sql

-- pytania
select * from polls_question;

-- odpowiedzi
select * from polls_choice;



-- systemowe

-- migrations
select * from django_migrations;

select * from django_admin_log;

-- zmiany do bazy

-- insert into polls_choice (choice_text, votes, question_id) values ('PG+', 0, 2);
-- insert into polls_choice (choice_text, votes, question_id) values ('PZ+', 0, 2);
-- insert into polls_choice (choice_text, votes, question_id) values ('PK', 0, 2);
-- insert into polls_choice (choice_text, votes, question_id) values ('PD+', 0, 2);


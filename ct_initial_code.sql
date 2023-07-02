DROP DATABASE ct_full_practice;
CREATE DATABASE ct_full_practice;
USE ct_full_practice;
CREATE TABLE game_rankings (
Game varchar(255),
Ranking int
);
INSERT INTO game_rankings (Game, Ranking) values ('Portal', 1),('Europa Universalis 4',2),('Factorio',3),('Pultocracy',4);
select Game from game_rankings WHERE Ranking = 3;
select * from game_rankings;
#SET SQL_SAFE_UPDATES=1;
#DELETE FROM game_rankings WHERE Game='portal';
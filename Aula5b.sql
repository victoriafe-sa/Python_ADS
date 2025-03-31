create database facsenac;
use facsenac;

create table editora (
	codeditora int not null primary key,
    nome_editora varchar (30) not null
);

create table livro(
	cod int not null primary key auto_increment,
    nome_livro varchar (50) not null,
    autor char (50),
    codeidt int,
    FOREIGN KEY (codeidt) REFERENCES editora (codeditora)
);

insert into editora values 
(10, 'novatech'),
(11,'palmer'),
(12,'campos'),
(13,'moderna');

insert into livro (nome_livro,autor,codeidt) values 
('Farenheit 51','Alberto Santos', 11),
('lavajato','Joice Hasselman', 12), 
('Fantasma da Hopera','John Liber', 12),
('Passando a limpo','Deltan Dallagnol', 10), 
('Voar e a 2. melhor coisa do mundo','Cmte.Dato De Oliveira', 13);

# PARA CONFERIR
select * from editora, livro;

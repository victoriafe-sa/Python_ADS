CREATE DATABASE db_senac;
use db_senac;

CREATE TABLE usuario(
	coduser INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    cidade CHAR(30) NOT NULL DEFAULT 'Brasília',
    uf CHAR(2) DEFAULT 'DF',
    data_cadastro DATE
);

show tables;
select*from usuario;

INSERT INTO usuario (coduser, nome, senha, cidade, uf,data_cadastro) VALUES
    (NULL, 'Arnaldo', 'senac123', DEFAULT, DEFAULT,'2025-03-31'),
    (NULL, 'Fonseca', 'senac123', DEFAULT, DEFAULT,'2025-01-31'),
    (NULL, 'Jose', 'senac123', 'São Paulo','SP','2024-03-31'),
    (NULL, 'Ana Paula', 'senac123', 'Ceilandia', DEFAULT,'2025-08-31'), 
    (NULL, 'Paula', 'senac123', 'Ceilandia', DEFAULT,'2025-03-30');

DESCRIBE usuario;
SELECT * FROM usuario;

delete from `db_senac`.`usuario`
where coduser = 3;
select * from usuario
-- Active: 1770140839866@@127.0.0.1@3306@universidade
CREATE DATABASE universidade;
USE universidade;
CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    cpf CHAR(11) UNIQUE NOT NULL,
    telefone CHAR(12) UNIQUE,
    endereco VARCHAR(150),
    matricula BOOLEAN DEFAULT TRUE 
);
SELECT 
    id,
    nome,
    email,
    cpf,
    telefone,
    endereco,
    matricula
FROM
    alunos;
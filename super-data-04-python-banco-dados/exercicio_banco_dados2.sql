# Ex. 02: Criar um novo banco de dados chamado helpdesk:
# - Criar uma tabela de categorias com: nome, cor da categoria (hexadecimal) e id
#       Fazer o consultar categorias no python
#       Fazer o cadastro da categoria no python
# - Criar uma tabela de tickets com os seguintes campos:
# id int
# numero_protocolo: str
# titulo: str
# descricao: str
# --status: str(ABERTO, EM_ANALISE, RESOLVIDO, CANCELADO)
# prioridade: str(BAIXA, MEDIA, ALTA)
# setor: (TI, RH, FINANCEIRO, ADMINISTRATIVO, MANUTENCAO)
# descricao_solucao: str
# data_criacao: datetime
# Fazer o CRUD em python para permitir interagir com a tabela de tickets

CREATE DATABASE helpdesk_db;

USE helpdesk_db;

CREATE TABLE categorias(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    cor_categoria CHAR(6)
);

CREATE TABLE tickets(
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero_protocolo VARCHAR(20),
    titulo VARCHAR(50),
    descricao VARCHAR(100),
    status VARCHAR(20) CONSTRAINT chk_status CHECK (status IN ('ABERTO', 'EM_ANALISE', 'RESOLVIDO', 'CANCELADO')),
    prioridade VARCHAR(10) CONSTRAINT chk_prioridade CHECK (prioridade IN ('BAIXA', 'MEDIA', 'ALTA')),
    setor VARCHAR(20) CONSTRAINT chk_setor CHECK (setor IN ('TI', 'RH', 'FINANCEIRO', 'ADMINISTRATIVO', 'MANUTENCAO')),
    descricao_solucao VARCHAR(100),
    data_criacao DATETIME
);
USE loja_db;

CREATE TABLE fornecedores(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(100) NOT NULL,
    nome_fantasia VARCHAR(100) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    numero VARCHAR(10)
);

CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    endereco VARCHAR(200),
    telefone VARCHAR(15),
    email VARCHAR(50),
    limite_credito DECIMAL(10,2) DEFAULT 0.00
);


CREATE TABLE produtos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(200),
    nome VARCHAR(50) NOT NULL
);

INSERT INTO fornecedores (
    cnpj,
    razao_social,
    nome_fantasia,
    cep,
    numero
) VALUES (
    '12.345.678/0001-90',
    'Empresa Exemplo Ltda',
    'Empresa Exemplo',
    '88000-000',
    '123'
);

ALTER TABLE produtos 
ADD COLUMN id_fornecedor INT,
ADD CONSTRAINT produtos_fornecedores_fk
FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id);
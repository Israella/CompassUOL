-- Tabela tb_cliente
CREATE TABLE tb_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50)
);

-- Tabela tb_carro
CREATE TABLE tb_carro (
    idCarro INT PRIMARY KEY,
    kmCarro DECIMAL(10, 2),
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(100),
    modeloCarro VARCHAR(100),
    anoCarro INT,
    idcombustivel INT
);

-- Tabela tb_locacao
CREATE TABLE tb_locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10, 2),
    dataEntrega DATE,
    horaEntrega TIME
);

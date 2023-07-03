-- tabela de fatos: tabela que contém as métricas numéricas e as chaves estrangeiras para as dimensões.

CREATE TABLE dim_locacao (
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

-- tabelas de dimensões: tabelas que contêm os atributos descritivos relacionados a cada dimensão.

CREATE TABLE dim_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50)
);

CREATE TABLE dim_carro (
    idCarro INT PRIMARY KEY,
    kmCarro DECIMAL(10, 2),
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(100),
    modeloCarro VARCHAR(100),
    anoCarro INT,
    idcombustivel INT
);

CREATE TABLE dim_vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor CHAR(1),
    estadoVendedor VARCHAR(50)
);

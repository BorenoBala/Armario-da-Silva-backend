CREATE TABLE equipe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR (100) not null,
    escudo VARCHAR (255) not null,

)


CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) not null,
    email VARCHAR(100) not null,
    senha VARCHAR(100) not null,
    cpf VARCHAR (20) not null,
    endereco VARCHAR(100) not null,
    data_nascimento date not null,
    time_id INT,
    FOREIGN KEY (time_id) references equipe(id)
    
);

CREATE TABLE endereco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    logradouro VARCHAR(100) not null,
    rua VARCHAR(100) not null,
    numero VARCHAR(10) not null,
    bairro VARCHAR(100) not null,
    cidade VARCHAR(100) not null,
    estado VARCHAR(50) not null,
    cep VARCHAR(10) not null,
    enderecoID INT
    FOREIGN KEY (enderecoID) references usuario(endereco)
);

CREATE TABLE agendamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_agendamento date not null,
    local_agendamento VARCHAR(100) not null,
    horario time not null,
    agendamentoID INT,
    FOREIGN KEY (agendamentoID) references usuario(id)
);

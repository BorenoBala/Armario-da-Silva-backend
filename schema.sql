CREATE TABLE equipe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    escudo VARCHAR(255) NOT NULL
);


CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    cpf VARCHAR(20) NOT NULL,
    endereco VARCHAR(100) NOT NULL UNIQUE,  
    data_nascimento DATE NOT NULL,
    time_id INT,
    FOREIGN KEY (time_id) REFERENCES equipe(id)
);

CREATE TABLE endereco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    logradouro VARCHAR(100) NOT NULL,
    rua VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    endereco VARCHAR(100),
    FOREIGN KEY (endereco) REFERENCES usuario(endereco)
);

CREATE TABLE agendamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_agendamento DATE NOT NULL,
    local_agendamento VARCHAR(100) NOT NULL,
    horario TIME NOT NULL,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE estatisticas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    gols INT,
    assistencias INT,
    cartao_amarelo INT,
    cartao_vermelho INT,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);
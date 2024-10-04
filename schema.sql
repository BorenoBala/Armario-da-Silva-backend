CREATE TABLE equipe (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR (100) NOT NULL,
    escudo VARCHAR (255) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

CREATE TABLE usuario (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    cpf VARCHAR (20) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    equipe_id INT,
    FOREIGN KEY (equipe_id) references equipe(id),
);

CREATE TABLE juiz (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) references usuario(id)
);

CREATE TABLE endereco (

    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
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
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    data_agendamento DATE NOT NULL,
    local_agendamento VARCHAR(100) NOT NULL,
    horario TIME NOT NULL,
    valor float NOT NULL,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE estatisticas(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    partidas INT,
    vitorias INT,
    empates INT,
    derrotas INT,
    gols INT,
    assistencias INT,
    cartao_amarelo INT,
    cartao_vermelho INT,
    melhor_da_partida INT,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE estatisticas_equipe(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    partidas INT,
    vitorias INT,
    empates INT,
    derrotas INT,
    gols_feitos INT,
    gols_sofridos INT,
    maior_assistente VARCHAR(100),
    maior_goleador VARCHAR (100),
    cartoes_amarelos INT,
    cartoes_vermelhos INT
);
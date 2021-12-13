CREATE DATABASE IF NOT EXISTS master_python;
use master_python:

CREATE TABLE usuarios(
id          int(25) ,
nombre      varchar(100),
apellidos   varchar(255),
email       varchar(255) not null,
password    varchar(255) not null,
fecha       date,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
id          int(25) auto_increment not null,
usuarios_id int(25) not null,
titulo varchar(255) not null,
descripcion MEDIUMTEXT,
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario FOREIGN KEY(usuarios_id) REFERENCES usuarios(id) 
)ENGINE=InnoDb
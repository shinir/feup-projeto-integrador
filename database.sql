BEGIN TRANSACTION;

CREATE TABLE "Instituicao" (
	"codigo" INTEGER PRIMARY KEY,
	"nome" TEXT NOT NULL,
	"ensinoSuperior" BOOLEAN NOT NULL
);

CREATE TABLE "Curso" (
    "id" INTEGER PRIMARY KEY,
	"codigo" INTEGER NOT NULL,
	"nome" TEXT NOT NULL,
	"vagas" INTEGER NOT NULL,
    "ano" INTEGER NOT NULL,
	"instituicao" INTEGER NOT NULL,
	FOREIGN KEY(instituicao) REFERENCES Instituicao(codigo),
	UNIQUE(codigo, ano)
);

CREATE TABLE "Colocado" (
    "id" INTEGER PRIMARY KEY,
	"codigo" TEXT NOT NULL,
	"nome" TEXT NOT NULL,
	UNIQUE(codigo, nome)
);

CREATE TABLE "Candidatura" (
	"id" INTEGER NOT NULL,
	"codigo" TEXT NOT NULL,
	"nome" TEXT NOT NULL,
	"media"	TEXT NOT NULL,
	"opcao" INTEGER NOT NULL,
	"pi" INTEGER NOT NULL,
	"12ano"	INTEGER NOT NULL,
    "1011ano" INTEGER NOT NULL,
	UNIQUE(codigo, nome)
);

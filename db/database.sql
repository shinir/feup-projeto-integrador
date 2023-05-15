BEGIN TRANSACTION;

CREATE TABLE "Instituicao" (
	"codigo" TEXT PRIMARY KEY,
	"nome" TEXT NOT NULL,
	"ensinoSuperior" BOOLEAN NOT NULL
);

CREATE TABLE "Curso" (
    "id" INTEGER PRIMARY KEY,
	"codigo" TEXT NOT NULL,
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
	"curso" INT NOT NULL,
	FOREIGN KEY(curso) REFERENCES Curso(id),
	UNIQUE(codigo, nome, curso)
);

CREATE TABLE "Candidatura" (
	"id" INTEGER NOT NULL,
	"codigo" TEXT NOT NULL,
	"nome" TEXT NOT NULL,
	"media"	FLOAT NOT NULL,
	"opcao" INTEGER NOT NULL,
	"pi" FLOAT NOT NULL,
	"ano12"	FLOAT NOT NULL,
	"ano1011" FLOAT NOT NULL,
	"curso" INT NOT NULL,
	FOREIGN KEY(curso) REFERENCES Curso(id),
	UNIQUE(codigo, nome, curso)
);

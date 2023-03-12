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

CREATE TABLE "Aluno" (
    "id" INTEGER PRIMARY KEY,
	"codigo" TEXT NOT NULL,
	"nome" TEXT NOT NULL,
	"12ano"	INTEGER NOT NULL,
    "1011ano" INTEGER NOT NULL,
	UNIQUE(codigo, nome)
);

CREATE TABLE "Candidatura" (
	"media"	TEXT NOT NULL,
	"opcao" INTEGER NOT NULL,
	"colocado" BOOLEAN NOT NULL,
    "pi" INTEGER NOT NULL,
	"curso" INTEGER NOT NULL,
	"aluno" INTEGER NOT NULL,
	FOREIGN KEY(curso) REFERENCES Curso(id),
	FOREIGN KEY(aluno) REFERENCES Aluno(id),
	PRIMARY KEY(curso, aluno)
);

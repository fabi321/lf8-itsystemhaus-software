CREATE TABLE IF NOT EXISTS Benutzer(
    Benutzer_ID TEXT NOT NULL UNIQUE,
    Vorname TEXT,
    Name TEXT,
    Passwort TEXT NOT NULL,
    PRIMARY KEY(Benutzer_ID)
);

CREATE TABLE IF NOT EXISTS Gruppe(
    Gruppen_ID TEXT NOT NULL UNIQUE,
    Name TEXT NOT NULL,
    PRIMARY KEY (Gruppen_ID)
);

CREATE TABLE IF NOT EXISTS Benutzergruppe(
    Benutzer_ID TEXT NOT NULL UNIQUE REFERENCES Benutzer,
    Gruppen_ID TEXT NOT NULL UNIQUE REFERENCES Gruppe,
    PRIMARY KEY(Benutzer_ID, Gruppen_ID)
);

CREATE TABLE IF NOT EXISTS Rolle(
    Rollen_ID INTEGER NOT NULL UNIQUE,
    Name TEXT,
    PRIMARY KEY(Rollen_ID)
);

CREATE TABLE IF NOT EXISTS Gruppen_Rolle(
    Rollen_ID TEXT NOT NULL UNIQUE REFERENCES Rolle,
    Gruppen_ID TEXT NOT NULL UNIQUE REFERENCES Gruppe,
    PRIMARY KEY(Rollen_ID, Gruppen_ID)
);

CREATE TABLE IF NOT EXISTS Inventar(
    Inventar_ID INTEGER NOT NULL UNIQUE,
    Name TEXT,
    Menge INTEGER,
    Preis REAL,
    PRIMARY KEY(Inventar_ID)
);

CREATE TABLE IF NOT EXISTS Grundriss(
    Grundriss_ID INTEGER NOT NULL UNIQUE ,
    Name TEXT,
    Grundriss_Daten BLOB,
    PRIMARY KEY(Inventar_ID)
);

CREATE TABLE IF NOT EXISTS Platzierung(
    Platzierung_ID INTEGER NOT NULL UNIQUE,
    Inventar_ID INTEGER NOT NULL UNIQUE REFERENCES Inventar,
    Grundriss_ID INTEGER NOT NULL UNIQUE REFERENCES Grundriss,
    x REAL,
    y REAL,
    z REAL,
    Plaziert BOOLEAN,
    PRIMARY KEY(Platzierung_ID)
);



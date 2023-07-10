

CREATE TABLE "IntermicrobialInteraction" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	evidence_type TEXT NOT NULL, 
	reference TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "IntermicrobialInteractionCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "IntermicrobialInteraction_participants" (
	backref_id TEXT, 
	participants TEXT NOT NULL, 
	PRIMARY KEY (backref_id, participants), 
	FOREIGN KEY(backref_id) REFERENCES "IntermicrobialInteraction" (id)
);

CREATE TABLE "IntermicrobialInteraction_tax_id" (
	backref_id TEXT, 
	tax_id INTEGER NOT NULL, 
	PRIMARY KEY (backref_id, tax_id), 
	FOREIGN KEY(backref_id) REFERENCES "IntermicrobialInteraction" (id)
);

CREATE TABLE "IntermicrobialInteraction_sequence_id" (
	backref_id TEXT, 
	sequence_id TEXT, 
	PRIMARY KEY (backref_id, sequence_id), 
	FOREIGN KEY(backref_id) REFERENCES "IntermicrobialInteraction" (id)
);

CREATE TABLE "IntermicrobialInteraction_method_type" (
	backref_id TEXT, 
	method_type VARCHAR(11), 
	PRIMARY KEY (backref_id, method_type), 
	FOREIGN KEY(backref_id) REFERENCES "IntermicrobialInteraction" (id)
);

CREATE TABLE "IntermicrobialInteraction_participant_outcomes" (
	backref_id TEXT, 
	participant_outcomes VARCHAR(14), 
	PRIMARY KEY (backref_id, participant_outcomes), 
	FOREIGN KEY(backref_id) REFERENCES "IntermicrobialInteraction" (id)
);

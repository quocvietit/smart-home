-- Drop Table
DROP TABLE IF EXISTS public.device_configuration;
DROP TABLE IF EXISTS public.device_status;
DROP TABLE IF EXISTS public.device;
DROP TABLE IF EXISTS public.device_type;
DROP TABLE IF EXISTS public.device_location;
DROP TABLE IF EXISTS public.configuration;

-- Drop Sequence
DROP SEQUENCE IF EXISTS public.device_configuration_id_seq;
DROP SEQUENCE IF EXISTS public.device_status_id_seq;
DROP SEQUENCE IF EXISTS public.device_id_seq;
DROP SEQUENCE IF EXISTS public.device_type_id_seq;
DROP SEQUENCE IF EXISTS public.device_location_id_seq;
DROP SEQUENCE IF EXISTS public.configuration_id_seq;

-- Create Table
CREATE TABLE public.device_configuration (
    id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    key CHARACTER VARYING(255) NOT NULL,
	value CHARACTER VARYING(255) NOT NULL,
	created TIMESTAMP WITHOUT TIME ZONE,
	modified TIMESTAMP WITHOUT TIME ZONE
);

CREATE TABLE public.device_status (
    id INTEGER NOT NULL,
	device_id INTEGER NOT NULL,
    value CHARACTER VARYING(255) NOT NULL,
    time TIMESTAMP WITHOUT TIME ZONE
);

CREATE TABLE public.device (
    id INTEGER NOT NULL,
	type_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
	mqtt_topic CHARACTER VARYING(255) NOT NULL,
	socket_topic CHARACTER VARYING(255) NOT NULL,
	last_activity TIMESTAMP WITHOUT TIME ZONE,
	is_control BOOLEAN NOT NULL,
	is_enable BOOLEAN NOT NULL,
	is_connect BOOLEAN NOT NULL
);

CREATE TABLE public.device_type (
    id INTEGER NOT NULL,
    name CHARACTER VARYING(255) NOT NULL,
    description TEXT
);

CREATE TABLE public.device_location (
    id INTEGER NOT NULL,
    name CHARACTER VARYING(255) NOT NULL,
	description TEXT
);

CREATE TABLE public.configuration (
    id INTEGER NOT NULL,
    key CHARACTER VARYING(255) NOT NULL,
	value CHARACTER VARYING(255) NOT NULL,
	env CHARACTER VARYING(255) NOT NULL
);

-- Create sequence id
CREATE SEQUENCE public.device_configuration_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.device_configuration_id_seq OWNED BY public.device_configuration.id;
ALTER TABLE ONLY public.device_configuration ALTER COLUMN id SET DEFAULT nextval('public.device_configuration_id_seq'::regclass);

CREATE SEQUENCE public.device_status_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.device_status_id_seq OWNED BY public.device_status.id;
ALTER TABLE ONLY public.device_status ALTER COLUMN id SET DEFAULT nextval('public.device_status_id_seq'::regclass);

CREATE SEQUENCE public.device_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.device_id_seq OWNED BY public.device.id;
ALTER TABLE ONLY public.device ALTER COLUMN id SET DEFAULT nextval('public.device_id_seq'::regclass);

CREATE SEQUENCE public.device_type_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.device_type_id_seq OWNED BY public.device_type.id;
ALTER TABLE ONLY public.device_type ALTER COLUMN id SET DEFAULT nextval('public.device_type_id_seq'::regclass);

CREATE SEQUENCE public.device_location_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.device_location_id_seq OWNED BY public.device_location.id;
ALTER TABLE ONLY public.device_location ALTER COLUMN id SET DEFAULT nextval('public.device_location_id_seq'::regclass);

CREATE SEQUENCE public.configuration_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.configuration_id_seq OWNED BY public.configuration.id;
ALTER TABLE ONLY public.configuration ALTER COLUMN id SET DEFAULT nextval('public.configuration_id_seq'::regclass);

-- Add PK
ALTER TABLE ONLY public.device_configuration
    ADD CONSTRAINT device_configuration_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.device_status
    ADD CONSTRAINT device_status_pkey PRIMARY KEY (id);	

ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.device_type
    ADD CONSTRAINT device_type_pkey PRIMARY KEY (id),
    ADD CONSTRAINT device_type_name_key UNIQUE (name);

ALTER TABLE ONLY public.device_location
    ADD CONSTRAINT device_location_pkey PRIMARY KEY (id),
    ADD CONSTRAINT device_location_name_key UNIQUE (name);
	
ALTER TABLE ONLY public.configuration
    ADD CONSTRAINT configuration_pkey PRIMARY KEY (id);

-- Add FK
ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.device_type(id),
	ADD CONSTRAINT device_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.device_location(id);
	
ALTER TABLE ONLY public.device_configuration
    ADD CONSTRAINT device_configuration_id_fkey FOREIGN KEY (type_id) REFERENCES public.device_type(id);
	
ALTER TABLE ONLY public.device_status
    ADD CONSTRAINT device_status_id_fkey FOREIGN KEY (device_id) REFERENCES public.device(id);
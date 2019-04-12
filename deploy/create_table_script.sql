
DROP TABLE IF EXISTS public.history;
DROP TABLE IF EXISTS public.device;
DROP TABLE IF EXISTS public.type;
DROP SEQUENCE IF EXISTS public.history_id_seq;
DROP SEQUENCE IF EXISTS public.type_id_seq;
DROP SEQUENCE IF EXISTS public.device_id_seq;

-- Table

CREATE TABLE public.history (
    id integer NOT NULL,
    value text NOT NULL,
    "time" timestamp without time zone,
    device_id integer NOT NULL
);


CREATE TABLE public.device (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    last_activity timestamp without time zone,
    is_connect boolean NOT NULL,
    is_enable boolean NOT NULL,
    type_id integer NOT NULL
);


CREATE TABLE public.type (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    description text,
    note character varying,
    created timestamp without time zone,
    modified timestamp without time zone
);

CREATE SEQUENCE public.history_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.history_id_seq OWNED BY public.history.id;
ALTER TABLE ONLY public.history ALTER COLUMN id SET DEFAULT nextval('public.history_id_seq'::regclass);

CREATE SEQUENCE public.type_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.type_id_seq OWNED BY public.type.id;
ALTER TABLE ONLY public.type ALTER COLUMN id SET DEFAULT nextval('public.type_id_seq'::regclass);

CREATE SEQUENCE public.device_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
ALTER SEQUENCE public.device_id_seq OWNED BY public.device.id;
ALTER TABLE ONLY public.device ALTER COLUMN id SET DEFAULT nextval('public.device_id_seq'::regclass);

ALTER TABLE ONLY public.type
    ADD CONSTRAINT type_pkey PRIMARY KEY (id),
    ADD CONSTRAINT type_name_key UNIQUE (name);

ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_pkey PRIMARY KEY (id),
    ADD CONSTRAINT device_name_key UNIQUE (name);

ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_pkey PRIMARY KEY (id);
	
ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.type(id);
ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_device_id_fkey FOREIGN KEY (device_id) REFERENCES public.device(id);
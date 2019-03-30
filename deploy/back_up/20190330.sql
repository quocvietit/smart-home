PGDMP         0                w         	   smarthome    11.2    11.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    16579 	   smarthome    DATABASE     �   CREATE DATABASE smarthome WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE smarthome;
             postgres    false            �            1259    24870    device    TABLE     �   CREATE TABLE public.device (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    last_activity timestamp without time zone,
    is_connect boolean NOT NULL,
    is_enable boolean NOT NULL,
    type_id integer NOT NULL
);
    DROP TABLE public.device;
       public         postgres    false            �            1259    24868    device_id_seq    SEQUENCE     �   CREATE SEQUENCE public.device_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.device_id_seq;
       public       postgres    false    200                       0    0    device_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.device_id_seq OWNED BY public.device.id;
            public       postgres    false    199            �
           2604    24873 	   device id    DEFAULT     f   ALTER TABLE ONLY public.device ALTER COLUMN id SET DEFAULT nextval('public.device_id_seq'::regclass);
 8   ALTER TABLE public.device ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    200    199    200                      0    24870    device 
   TABLE DATA               Y   COPY public.device (id, name, last_activity, is_connect, is_enable, type_id) FROM stdin;
    public       postgres    false    200   S                  0    0    device_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.device_id_seq', 1, false);
            public       postgres    false    199            �
           2606    24877    device device_name_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_name_key UNIQUE (name);
 @   ALTER TABLE ONLY public.device DROP CONSTRAINT device_name_key;
       public         postgres    false    200            �
           2606    24875    device device_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.device DROP CONSTRAINT device_pkey;
       public         postgres    false    200            �
           2606    24878    device device_type_id_fkey    FK CONSTRAINT     x   ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.type(id);
 D   ALTER TABLE ONLY public.device DROP CONSTRAINT device_type_id_fkey;
       public       postgres    false    200               .   x�3����M���,�L�4�2�q�pr	r�	q��qqq ��	�     
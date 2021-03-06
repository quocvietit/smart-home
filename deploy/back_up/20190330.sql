PGDMP     *    	                w         	   smarthome    11.2    11.2      "           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            #           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            $           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            %           1262    16579 	   smarthome    DATABASE     �   CREATE DATABASE smarthome WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE smarthome;
             postgres    false            �            1259    24850    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         postgres    false            �            1259    24870    device    TABLE     �   CREATE TABLE public.device (
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
       public       postgres    false    200            &           0    0    device_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.device_id_seq OWNED BY public.device.id;
            public       postgres    false    199            �            1259    24885    history    TABLE     �   CREATE TABLE public.history (
    id integer NOT NULL,
    value text NOT NULL,
    "time" timestamp without time zone,
    device_id integer NOT NULL
);
    DROP TABLE public.history;
       public         postgres    false            �            1259    24883    history_id_seq    SEQUENCE     �   CREATE SEQUENCE public.history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.history_id_seq;
       public       postgres    false    202            '           0    0    history_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.history_id_seq OWNED BY public.history.id;
            public       postgres    false    201            �            1259    24857    type    TABLE     �   CREATE TABLE public.type (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    description text,
    note character varying,
    created timestamp without time zone,
    modified timestamp without time zone
);
    DROP TABLE public.type;
       public         postgres    false            �            1259    24855    type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.type_id_seq;
       public       postgres    false    198            (           0    0    type_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.type_id_seq OWNED BY public.type.id;
            public       postgres    false    197            �
           2604    24873 	   device id    DEFAULT     f   ALTER TABLE ONLY public.device ALTER COLUMN id SET DEFAULT nextval('public.device_id_seq'::regclass);
 8   ALTER TABLE public.device ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    200    199    200            �
           2604    24888 
   history id    DEFAULT     h   ALTER TABLE ONLY public.history ALTER COLUMN id SET DEFAULT nextval('public.history_id_seq'::regclass);
 9   ALTER TABLE public.history ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    202    201    202            �
           2604    24860    type id    DEFAULT     b   ALTER TABLE ONLY public.type ALTER COLUMN id SET DEFAULT nextval('public.type_id_seq'::regclass);
 6   ALTER TABLE public.type ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    198    197    198                      0    24850    alembic_version 
   TABLE DATA               6   COPY public.alembic_version (version_num) FROM stdin;
    public       postgres    false    196   �!                 0    24870    device 
   TABLE DATA               Y   COPY public.device (id, name, last_activity, is_connect, is_enable, type_id) FROM stdin;
    public       postgres    false    200   �!                 0    24885    history 
   TABLE DATA               ?   COPY public.history (id, value, "time", device_id) FROM stdin;
    public       postgres    false    202   �!                 0    24857    type 
   TABLE DATA               N   COPY public.type (id, name, description, note, created, modified) FROM stdin;
    public       postgres    false    198   
"       )           0    0    device_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.device_id_seq', 1, false);
            public       postgres    false    199            *           0    0    history_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.history_id_seq', 1, false);
            public       postgres    false    201            +           0    0    type_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.type_id_seq', 1, false);
            public       postgres    false    197            �
           2606    24854 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public         postgres    false    196            �
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
           2606    24893    history history_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.history DROP CONSTRAINT history_pkey;
       public         postgres    false    202            �
           2606    24867    type type_name_key 
   CONSTRAINT     M   ALTER TABLE ONLY public.type
    ADD CONSTRAINT type_name_key UNIQUE (name);
 <   ALTER TABLE ONLY public.type DROP CONSTRAINT type_name_key;
       public         postgres    false    198            �
           2606    24865    type type_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.type
    ADD CONSTRAINT type_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.type DROP CONSTRAINT type_pkey;
       public         postgres    false    198            �
           2606    24878    device device_type_id_fkey    FK CONSTRAINT     x   ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.type(id);
 D   ALTER TABLE ONLY public.device DROP CONSTRAINT device_type_id_fkey;
       public       postgres    false    2711    200    198            �
           2606    24894    history history_device_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_device_id_fkey FOREIGN KEY (device_id) REFERENCES public.device(id);
 H   ALTER TABLE ONLY public.history DROP CONSTRAINT history_device_id_fkey;
       public       postgres    false    200    202    2715                  x�3��H16 "KK�=... &��         .   x�3����M���,�L�4�2�q�pr	r�	q��qqq ��	�            x������ � �         )   x�3�,I�-����".#�W� � ǐ� W�h� ӑ	&     
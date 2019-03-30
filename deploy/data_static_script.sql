INSERT INTO public.type(id, name, description, note, created, modified)
	VALUES (1,'TEMPERATURE', '', '', now(), now());
INSERT INTO public.type(id, name, description, note, created, modified)
	VALUES (2,'LIGHT', '', '', now(), now());
INSERT INTO public.type(id, name, description, note, created, modified)
	VALUES (3,'GAS', '', '', now(), now());
INSERT INTO public.type(id, name, description, note, created, modified)
	VALUES (4,'FLASH_LIGHT', '', '', now(), now());

	
INSERT INTO public.device(
	id, name, last_activity, is_connect, is_enable, type_id)
	VALUES (1, 'TEMPERATURE_HOME', now(), true, false, 1);
INSERT INTO public.device(
	id, name, last_activity, is_connect, is_enable, type_id)
	VALUES (2, 'LIGHT_HOME', now(), true, false, 2);
INSERT INTO public.device(
	id, name, last_activity, is_connect, is_enable, type_id)
	VALUES (3, 'GAS_HOME', now(), true, false, 3);
INSERT INTO public.device(
	id, name, last_activity, is_connect, is_enable, type_id)
	VALUES (4, 'FLASH_LIGHT_HOME', now(), true, false, 4);
	

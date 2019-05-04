INSERT INTO public.device_type(id, name, description)
	VALUES (1,'TEMPERATURE', 'Nhiệt độ');
INSERT INTO public.device_type(id, name, description)
	VALUES (2,'HUMIDITY', 'Độ ẩm');
INSERT INTO public.device_type(id, name, description)
	VALUES (3,'LIGHT', 'Độ sáng');
INSERT INTO public.device_type(id, name, description)
	VALUES (4,'GAS', 'Khí gas');
INSERT INTO public.device_type(id, name, description)
	VALUES (5,'FLASH_LIGHT', 'Trạng thái bóng đèn');

INSERT INTO public.device_location(id, name, description)
	VALUES (1,'LIVING_ROOM', 'Phòng khách');
	
INSERT INTO public.device(
	id, type_id, location_id, mqtt_topic, socket_topic,last_activity, is_connect, is_enable, is_control)
	VALUES (1, 1, 1, 'LIVINGROOM/TEMPERATURE', 'LIVINGROOM/TEMPERATURE', now(), true, true, false );
INSERT INTO public.device(
	id, type_id, location_id, mqtt_topic, socket_topic, last_activity, is_connect, is_enable, is_control)
	VALUES (2, 2, 1, 'LIVINGROOM/HUMIDITY', 'LIVINGROOM/HUMIDITY', now(), true, true, false );
INSERT INTO public.device(
	id, type_id, location_id, mqtt_topic, socket_topic, last_activity, is_connect, is_enable, is_control)
	VALUES (3, 3, 1, 'LIVINGROOM/LIGHT', 'LIVINGROOM/LIGHT', now(), true, true, false );
INSERT INTO public.device(
	id, type_id, location_id, mqtt_topic, socket_topic, last_activity, is_connect, is_enable, is_control)
	VALUES (4, 4, 1, 'LIVINGROOM/GAS', 'LIVINGROOM/GAS', now(), true, true, false );
INSERT INTO public.device(
	id, type_id, location_id, mqtt_topic, socket_topic, last_activity, is_connect, is_enable, is_control)
	VALUES (5, 5, 1, 'LIVINGROOM/FLASH_LIGHT', 'LIVINGROOM/FLASH_LIGHT', now(), true, true, false );
INSERT INTO public.device(
	id, type_id, location_id, mqtt_topic, socket_topic, last_activity, is_connect, is_enable, is_control)
	VALUES (6, 5, 1, 'LIVINGROOM/FLASH_LIGHT/CONTROL', '', now(), true, true, true );


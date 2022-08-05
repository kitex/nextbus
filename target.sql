//https://www.metrotransit.org/nextrip
create database target;

create schema metrotransit;

CREATE TABLE metrotransit.routes (
	route_id integer NULL,
	agency_id integer NULL,
	route_short_name integer NULL,
	route_long_name varchar(50) NULL,
	route_desc varchar(50) NULL,
	route_type integer NULL,
	route_url varchar(50) NULL,
	route_color varchar(50) NULL,
	route_text_color varchar(50) NULL,
	route_sort_order integer NULL
);

CREATE TABLE metrotransit.stops (
	stop_id integer NULL,
	stop_code integer NULL,
	stop_name varchar(50) NULL,
	stop_desc varchar(50) NULL,
	stop_lat real NULL,
	stop_lon real NULL,
	stop_url varchar(50) NULL,
	location_type integer NULL,
	wheelchair_boarding integer NULL,
	platform_code varchar(50) NULL
);


SELECT * FROM metrotransit.routes r where route_desc  like   '%Express%';

SELECT * FROM metrotransit.routes r;

SELECT * FROM metrotransit.stops r  where stop_name ='Target Field Station Platform 1' ;
SELECT * FROM metrotransit.stops r where stop_name  like '%Hwy 252%' order by stop_name ;

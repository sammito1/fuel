create table "UserCredentials"
(
	user_id serial
		constraint usercredentials_pk
			primary key,
	hashed_password varchar
);

create table "ClientInformation"
(
	client_id integer not null
		constraint clientinformation_pk
			primary key,
	user_id integer
		constraint user_id_fk
			references "UserCredentials",
	name text,
	address text,
	city text,
	state text,
	email text,
	zipcode varchar(5)
);

create table "FuelQuote"
(
	quote_id int
		constraint fuelquote_pk
			primary key,
	user_id int
		constraint user_id_fk
			references "UserCredentials",
	price float,
	date date,
	address text,
	gallons int,
	total_price float
);



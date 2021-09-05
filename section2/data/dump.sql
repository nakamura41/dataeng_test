SET check_function_bodies = false;

CREATE SCHEMA dealership;

SET search_path TO pg_catalog,public,dealership;

CREATE SEQUENCE dealership.car_pk_seq
	INCREMENT BY 1
	MINVALUE 0
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;

CREATE SEQUENCE dealership.customer_pk_seq
	INCREMENT BY 1
	MINVALUE 0
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;

CREATE SEQUENCE dealership.salesperson_pk_seq
	INCREMENT BY 1
	MINVALUE 0
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;

CREATE SEQUENCE dealership.sale_pk_seq
	INCREMENT BY 1
	MINVALUE 0
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;

CREATE TABLE dealership.Car(
	Id bigint NOT NULL DEFAULT nextval('dealership.car_pk_seq'::regclass),
	Name text,
    Model text,
    Manufacturer text,
    SerialNumber text,
    Weight numeric,
    Price numeric,
	CONSTRAINT pk_car_id PRIMARY KEY (Id)
);

CREATE TABLE dealership.Salesperson(
	Id bigint NOT NULL DEFAULT nextval('dealership.salesperson_pk_seq'::regclass),
	Name text,
	CONSTRAINT pk_salesperson_id PRIMARY KEY (Id)
);

CREATE TABLE dealership.Customer(
	Id bigint NOT NULL DEFAULT nextval('dealership.customer_pk_seq'::regclass),
	Name text,
	CONSTRAINT pk_customer_id PRIMARY KEY (Id)
);

CREATE TABLE dealership.Sale(
	Id bigint NOT NULL DEFAULT nextval('dealership.sale_pk_seq'::regclass),
	SaleNumber text,
    CustomerPhoneNumber text,
    CarId bigint,
    CustomerId bigint,
    SalespersonId bigint,
    SaleDate TIMESTAMP,
	CONSTRAINT pk_sale_id PRIMARY KEY (Id)
);

ALTER TABLE dealership.Sale ADD CONSTRAINT Customer_fk FOREIGN KEY (CustomerId)
REFERENCES dealership.Customer (Id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE dealership.Sale ADD CONSTRAINT Car_fk FOREIGN KEY (CarId)
REFERENCES dealership.Car (Id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE dealership.Sale ADD CONSTRAINT Salesperson_fk FOREIGN KEY (SalespersonId)
REFERENCES dealership.Salesperson (Id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;

INSERT INTO dealership.Car(Name, Model, Manufacturer, SerialNumber, Weight, Price)
VALUES 
('Toyota Camry Hybrid', 'Camry', 'Toyota', 'CR00001', 1560, 137000),
('Honda Civic 2021', 'Civic', 'Honda', 'CR00002', 1284, 125000),
('Honda Jazz', 'Jazz', 'Honda', 'CR00003', 1410, 124000),
('Lamborghini Aventador', 'Aventador', 'Lamborghini', 'CR00004', 1525, 1498000);

INSERT INTO dealership.Customer(Name)
VALUES 
('Henry Golding'),
('Sarah Jessica Parker'),
('Michelle Yeoh'),
('Ryan Goshling');

INSERT INTO dealership.Salesperson(Name)
VALUES 
('Mr. Bean'),
('Raj Kumar'),
('Teddy Bear'),
('Wolverine');

INSERT INTO dealership.Sale(SaleNumber, CustomerPhoneNumber, CarId, CustomerId, SalespersonId, SaleDate)
VALUES 
('S000001', '83184141', 4, 1, 3, '2021-09-02 19:10:25'),
('S000002', '93184141', 2, 4, 2, '2021-09-01 14:10:25'),
('S000003', '73184141', 3, 2, 2, '2021-09-04 12:10:25'),
('S000004', '63184141', 1, 3, 1, '2021-09-05 09:10:25');
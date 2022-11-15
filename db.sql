CREATE TABLE automobile (
    id          SERIAL PRIMARY KEY NOT NULL,
    year        SMALLINT NOT NULL,
    model       VARCHAR(100) NOT NULL,
    vin         VARCHAR(19) NOT NULL UNIQUE,
    color       VARCHAR(20) NOT NULL
);

CREATE TABLE vehicle_model (
    id              SERIAL PRIMARY KEY NOT NULL,
    name            VARCHAR(50) NOT NULL,
    manufacturer    VARCHAR(50) NOT NULL,
    picture_url     VARCHAR(256)
);

CREATE TABLE product (
    id          SERIAL PRIMARY KEY NOT NULL,
    product     VARCHAR(50) NOT NULL,
    price       NUMERIC(10,3) NOT NULL
);

INSERT INTO automobile(year, model, vin, color)
VALUES('2000', 'Corolla', 'ASDLKJ190', 'Silver');

INSERT INTO product(product, price)
VALUES('Big hats', '2.00');

INSERT INTO product(product, price)
VALUES('Frog statues', '3.50');

INSERT INTO product(product, price)
VALUES('Little boops', '10.00');


UPDATE product
SET price = price * 1.5;


CREATE TABLE automobile_model (
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  manufacturer_id INT NOT NULL REFERENCES manufacturer(id)
);

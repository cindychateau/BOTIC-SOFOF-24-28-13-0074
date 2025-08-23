SET autocommit = 0;

START TRANSACTION; -- Comenzamos con la transacción
UPDATE cuentas
SET saldo = saldo + 501
WHERE id = 1;

UPDATE cuentas
SET saldo = saldo - 501
WHERE id = 2;

SELECT "Antes del rollback" AS estado, cuentas.* FROM cuentas;

ROLLBACK; -- Regresa a los datos anteriores

SELECT * FROM cuentas;

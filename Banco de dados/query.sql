SELECT * FROM clientes

SELECT setval(
    pg_get_serial_sequence('clientes', 'id_cliente'),
    (SELECT MAX(id_cliente) FROM clientes)
);
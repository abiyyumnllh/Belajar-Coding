CREATE TABLE pelanggan (
    id_pelanggan INTEGER PRIMARY KEY,
    nama TEXT NOT NULL,
    layanan TEXT,
    harga INTEGER
);


INSERT INTO pelanggan (id_pelanggan, nama, layanan, harga)
VALUES (3, 'Abiyyu', 'Haircut Reguler', 25000)

UPDATE pelanggan
SET layanan = 'Haircut + Braids'
WHERE id_pelanggan = 4;

SELECT layanan, harga
FROM pelanggan
WHERE layanan LIKE '%Haircut%' AND harga > 50000

SELECT * FROM pelanggan;
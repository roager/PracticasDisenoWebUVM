const { Client } = require('pg');

// Configuración de la conexión
const client = new Client({
  user: 'postgres',             // Nombre de usuario
  host: 'localhost',            // Dirección del servidor (puede ser 'localhost' o la IP)
  database: 'restaurante', // Nombre de la base de datos
  password: 'Post2025%',    // Contraseña del usuario
  port: 5432,                   // Puerto de PostgreSQL (el predeterminado es 5432)
});

// Conectarse a la base de datos
client.connect()
  .then(() => {
    console.log('Conectado a la base de datos');
    
    // Realizar consultas después de la conexión (ejemplo de SELECT)
    return client.query('SELECT * FROM menuplatillos');
  })
  .then((res) => {
    console.log('Resultado de la consulta:', res.rows); // Mostrar los resultados de la consulta
  })
  .catch((err) => {
    console.error('Error en la conexión o en la consulta:', err.stack);
  })
  .finally(() => {
    // Cerrar la conexión una vez finalizada
    client.end();
  });

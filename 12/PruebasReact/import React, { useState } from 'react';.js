import React, { useState } from 'react';

function Car() {
  // Usamos el hook useState para manejar el estado del coche
  const [marca, setMarca] = useState('Toyota');
  const [modelo, setModelo] = useState('Corolla');
  const [año, setAño] = useState(2020);

  const cambiarModelo = () => {
    setModelo('Camry');
  };

  return (
    <div>
      <h1>Detalles del coche</h1>
      <p>Marca: {marca}</p>
      <p>Modelo: {modelo}</p>
      <p>Año: {año}</p>
      <button onClick={cambiarModelo}>Cambiar modelo</button>
    </div>
  );
}

export default Car;
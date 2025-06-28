import React, { useState } from 'react';

const Car = ({ color, frenos, motor }) => {
  const [marca, setMarca] = useState('Toyota');
  const [modelo, setModelo] = useState('Corolla');
  const [año, setAño] = useState(2022);

  const cambiarMarca = () => {
    setMarca('BMW');
  };

  return (
    <div style={styles.carContainer}>
      <h2>{marca}</h2>
      <p>Modelo: {modelo}</p>
      <p>Año: {año}</p>
      {/* <p>Color: {color}</p>
      <p>Frenos: {frenos}</p>
      */}
      <button onClick={cambiarMarca}>Cambiar marca</button>
    </div>
  );
};

// Estilos para mejorar el diseño
const styles = {
  carContainer: {
    border: '1px solid gray',
    padding: '10px',
    borderRadius: '8px',
    width: '200px',
    textAlign: 'center',
  },
};
export default Car;

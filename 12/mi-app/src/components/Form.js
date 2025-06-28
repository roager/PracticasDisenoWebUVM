import React, { useState } from 'react';

function MyForm() {
  // Estado para almacenar los valores de los campos
  const [formData, setFormData] = useState({
    name: '',
    email: '',
  });

  // Manejar el cambio en los campos de entrada
  const handleChange = (event) => {
    // ...prevData asegura que las demás propiedades se mantengan intactas.
    const t = (prevData) => ({
      ...prevData,
      [event.target.name]: event.target.value,
    });
    setFormData(t);
  };

  // Manejar el envío del formulario
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Datos enviados:', formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Nombre:</label>
        <input
          type="text"
          id="name"
          name="name"
          // El valor está controlado por el estado
          value={formData.name}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="email">Correo electrónico:</label>
        <input
          type="email"
          id="email"
          name="email"
          // El valor está controlado por el estado
          value={formData.email}
          onChange={handleChange}
        />
      </div>
      <button type="submit">Enviar</button>
    </form>
  );
}

export default MyForm;

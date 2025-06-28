import React, { Component } from 'react';

class Car extends Component {
  // Constructor para inicializar el estado
  constructor(props) {
    super(props);
    this.state = {
      marca: 'Toyota',
      modelo: 'Corolla',
      año: 2020,
    };
  }

  // Método para actualizar el modelo del coche
  cambiarModelo = () => {
    this.setState({ modelo: 'Camry' });
  };
}

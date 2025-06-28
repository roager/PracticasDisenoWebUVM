import React from 'react';
import ReactDOM from 'react-dom';
import Car from './components/Car';
import MyForm from './components/Form';

function App() {
  return (
    <div style={styles.container}>
      <Car />
      <MyForm />
    </div>
  );
}

const styles = {
  container: {
    display: 'flex', // Centrar horizontalmente
    justifyContent: 'center',
    alignItems: 'center', // Alinear verticalmente
    gap: '20px', // Espacio
    padding: '20px',
  },
};
export default App;
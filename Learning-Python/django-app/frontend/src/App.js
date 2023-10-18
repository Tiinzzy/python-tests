import React from 'react';
import './App.css';
import ItemList from './components/ItemList';
import AddItem from './components/AddItem';

function App() {
  return (
    <div className="App">
      <ItemList />
      <AddItem />
    </div>
  );
}

export default App;

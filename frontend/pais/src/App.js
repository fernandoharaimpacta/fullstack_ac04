import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

import Home from './pages/Home';
import AdicionarContinente from './pages/AdicionarContinente';
import ListarContinente from './pages/ListarContinente';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/adicionarcontinente" element={<AdicionarContinente />}></Route>
        <Route path="/listarcontinente" element={<ListarContinente />}></Route>
      </Routes>
    </Router>
  );
}

export default App;

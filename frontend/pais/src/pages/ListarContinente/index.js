import Header from "../../components/Header";
import {useEffect, useState, useRef} from 'react';

function ExcluirContinente(id) {
    alert(id);
}

function ListarContinente() {
    const [list, setList] = useState([]);
    useEffect(()=>{
        fetch('http://127.0.0.1:9000/v1/continente/listar_continentes')
            .then(response => response.json())
            .then(response => response.continentes)
            .then(setList);
    }, []);

    return (
        <div>
            <Header />

            <div>
                {list.map(continente => 
                <div>
                    <div key={continente.id}>{continente.nome}</div>
                    <button onClick={() => ExcluirContinente(continente.id)}>Excluir</button>
                </div>
                )}
            </div>
        </div>
    );
}

export default ListarContinente;
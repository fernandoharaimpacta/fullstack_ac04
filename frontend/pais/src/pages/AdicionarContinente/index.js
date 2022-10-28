import Header from "../../components/Header";

function CadastrarContinente(event) {
    event.preventDefault();
    const requestOptions = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({"nome": document.getElementById("continente").value}),
      mode: 'cors'
    };
    const request = new Request("http://127.0.0.1:9000/v1/continente/adicionar_continente", requestOptions);
  
    fetch(request)
      .then((response) => response.json())
      .then((data) => {
        if(data) {
          document.getElementById("continente").value = '';
          console.log(data);
          alert('Continente ' + data.continente.nome + ' foi salvo com id ' + data.continente.continente_id);
        }
      })
  }

function AdicionarContinente() {
    return (
        <div>
            <Header />

            <form>
                <label>Continente</label>
                <input id="continente" name="continente"></input><br />
                <button onClick={CadastrarContinente}>Salvar</button>
            </form>
        </div>
    );
}

export default AdicionarContinente;
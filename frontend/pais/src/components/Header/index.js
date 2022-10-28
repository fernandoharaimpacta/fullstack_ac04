import { Link } from "react-router-dom";

function Header() {
    return (
        <header>
            <div>
                <nav>
                    <ul class="menu">
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/adicionarcontinente">Adicionar Continente</Link></li>
                        <li><Link to="/listarcontinente">Listar Continente</Link></li>
                    </ul>
                </nav>
            </div>
            <br />
            <br />
            <br />
            <br />
        </header>
    );
}

export default Header;
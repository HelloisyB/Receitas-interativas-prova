// Mostra menu principal após clicar em "Continuar"
function mostrarMenu() {
  document.getElementById('home').style.display = 'none';
  document.getElementById('menu-principal').style.display = 'block';
}

// Mostra seção Buscar
function mostrarBuscar() {
  esconderSecoes();
  document.getElementById('buscar').style.display = 'block';
  buscarReceitas();
}

// Mostra seção Adicionar Receita
function mostrarAdicionar() {
  esconderSecoes();
  document.getElementById('adicionar').style.display = 'block';
}

// Mostra Lista de Compras
function mostrarCarrinho() {
  esconderSecoes();
  document.getElementById('carrinho').style.display = 'block';

  // Lista de compras é um array de objetos { nomeReceita, ingrediente }
  const lista = JSON.parse(localStorage.getItem("lista_compras")) || [];
  const ul = document.getElementById("lista-compras");
  ul.innerHTML = "";

  if (lista.length === 0) {
    ul.innerHTML = "<li>Sem itens na lista.</li>";
    return;
  }

  // Organizar ingredientes agrupados pelo nome da receita
  const agrupado = {};

  lista.forEach(item => {
    if (!agrupado[item.nomeReceita]) {
      agrupado[item.nomeReceita] = {};
    }
    agrupado[item.nomeReceita][item.ingrediente] = (agrupado[item.nomeReceita][item.ingrediente] || 0) + 1;
  });

  // Para cada receita, criar um título com o nome e listar ingredientes com quantidade
  for (const nomeReceita in agrupado) {
    const liTitulo = document.createElement("li");
    liTitulo.style.fontWeight = "bold";
    liTitulo.textContent = nomeReceita;
    ul.appendChild(liTitulo);

    const ingredientes = agrupado[nomeReceita];
    for (const ingrediente in ingredientes) {
      const quantidade = ingredientes[ingrediente];
      const liIngrediente = document.createElement("li");
      liIngrediente.style.marginLeft = "20px";
      liIngrediente.textContent = `${ingrediente} x${quantidade}`;
      ul.appendChild(liIngrediente);
    }
  }
}

// Esconde todas as seções
function esconderSecoes() {
  document.getElementById('buscar').style.display = 'none';
  document.getElementById('adicionar').style.display = 'none';
  document.getElementById('carrinho').style.display = 'none';
}

// Limpa a lista de compras
function limparLista() {
  localStorage.removeItem("lista_compras");
  mostrarCarrinho();
}

// Salva a receita (com upload de imagem)
function salvarReceita() {
  const nome = document.getElementById('nome').value.trim();
  const ingredientes = document.getElementById('ingredientes').value.trim();
  const preparo = document.getElementById('preparo').value.trim();
  const tags = document.getElementById('tags').value.trim();
  const imagemInput = document.getElementById('imagem');

  if (!nome || !ingredientes || !preparo) {
    alert("Preencha todos os campos obrigatórios!");
    return;
  }

  let imagem = gerarImagemAutomatica(nome); // padrão

  if (imagemInput.files && imagemInput.files[0]) {
    const reader = new FileReader();
    reader.onload = function(e) {
      imagem = e.target.result;
      salvar();
    };
    reader.readAsDataURL(imagemInput.files[0]);
  } else {
    salvar();
  }

  function salvar() {
    const receita = {
      id: Date.now(),
      nome,
      ingredientes,
      preparo,
      tags,
      imagem,
      favorito: false,
      avaliacao: 0,
      comentarios: [],
      lista: ingredientes.split(',').map(i => i.trim())
    };

    const receitas = JSON.parse(localStorage.getItem("receitas")) || [];
    receitas.push(receita);
    localStorage.setItem("receitas", JSON.stringify(receitas));

    alert("Receita salva com sucesso!");
    document.getElementById('nome').value = "";
    document.getElementById('ingredientes').value = "";
    document.getElementById('preparo').value = "";
    document.getElementById('tags').value = "";
    document.getElementById('imagem').value = "";
  }
}

// Gera imagem automática se o usuário não enviar
function gerarImagemAutomatica(nome) {
  nome = nome.toLowerCase();
  if (nome.includes("pizza")) return "../img/pizza.jpg";
  if (nome.includes("hamburguer")) return "https://i.imgur.com/BYBQFBA.png";
  if (nome.includes("macarrao") || nome.includes("massa")) return "https://i.imgur.com/Mb4RwU3.png";
  if (nome.includes("bolo")) return "https://i.imgur.com/9vOQfZC.png";
  return "https://i.imgur.com/z5zDe5N.png";
}

// Busca receitas salvas
function buscarReceitas() {
  const termo = document.getElementById('busca').value.toLowerCase();
  const receitas = JSON.parse(localStorage.getItem("receitas")) || [];

  const resultados = receitas.filter(r =>
    r.nome.toLowerCase().includes(termo) ||
    r.ingredientes.toLowerCase().includes(termo) ||
    (r.tags && r.tags.toLowerCase().includes(termo))
  );

  let html = "";
  resultados.forEach(r => {
    const estrelas = "★".repeat(r.avaliacao) + "☆".repeat(5 - r.avaliacao);
    html += `
      <div>
        <img src="${r.imagem}" alt="${r.nome}" style="max-width: 300px; border-radius: 10px;" />
        <h3>${r.nome} ${r.favorito ? "★" : ""}</h3>
        <p><strong>Ingredientes:</strong> ${r.ingredientes}</p>
        <p><strong>Preparo:</strong> ${r.preparo}</p>
        <p><strong>Tags:</strong> ${r.tags}</p>
        <p><strong>Avaliação:</strong> ${estrelas}</p>
        <label>Avalie:
          <select onchange="avaliarReceita(${r.id}, this.value)">
            <option value="">--</option>
            <option value="1">1 estrela</option>
            <option value="2">2 estrelas</option>
            <option value="3">3 estrelas</option>
            <option value="4">4 estrelas</option>
            <option value="5">5 estrelas</option>
          </select>
        </label><br/>
        <button onclick="toggleFavorito(${r.id})">${r.favorito ? "Remover Favorito" : "Favoritar"}</button>
        <button onclick="adicionarListaCompras(${r.id})">Adicionar à lista de compras</button>
        <button onclick="excluirReceita(${r.id})">Excluir Receita</button>
        <div>
          <h4>Comentários</h4>
          <ul>${r.comentarios.map(c => `<li>${c}</li>`).join("")}</ul>
          <input type="text" placeholder="Deixe um comentário" onkeydown="if(event.key==='Enter') comentarReceita(${r.id}, this.value)" />
        </div>
      </div>
      <hr/>
    `;
  });

  document.getElementById('resultados').innerHTML = html || "<p>Nenhuma receita encontrada.</p>";
}

// Alterna favorito
function toggleFavorito(id) {
  let receitas = JSON.parse(localStorage.getItem("receitas")) || [];
  receitas = receitas.map(r => {
    if (r.id === id) r.favorito = !r.favorito;
    return r;
  });
  localStorage.setItem("receitas", JSON.stringify(receitas));
  buscarReceitas();
}

// Exclui receita
function excluirReceita(id) {
  if (confirm("Tem certeza que quer excluir essa receita?")) {
    let receitas = JSON.parse(localStorage.getItem("receitas")) || [];
    receitas = receitas.filter(r => r.id !== id);
    localStorage.setItem("receitas", JSON.stringify(receitas));
    buscarReceitas();
  }
}

// Avaliar receita
function avaliarReceita(id, valor) {
  const avaliacao = parseInt(valor);
  if (avaliacao < 1 || avaliacao > 5) return;

  let receitas = JSON.parse(localStorage.getItem("receitas")) || [];
  receitas = receitas.map(r => {
    if (r.id === id) {
      r.avaliacao = avaliacao;
    }
    return r;
  });

  localStorage.setItem("receitas", JSON.stringify(receitas));
  buscarReceitas();
}

// Comentar receita
function comentarReceita(id, texto) {
  const comentario = texto.trim();
  if (!comentario) return;

  let receitas = JSON.parse(localStorage.getItem("receitas")) || [];
  receitas = receitas.map(r => {
    if (r.id === id) {
      r.comentarios.push(comentario);
    }
    return r;
  });

  localStorage.setItem("receitas", JSON.stringify(receitas));
  buscarReceitas();
}

// Adiciona ingredientes da receita à lista de compras, junto com o nome da receita
function adicionarListaCompras(id) {
  const receitas = JSON.parse(localStorage.getItem("receitas")) || [];
  const receita = receitas.find(r => r.id === id);
  if (!receita) return;

  // lista_compras agora é array de objetos { nomeReceita, ingrediente }
  const lista = JSON.parse(localStorage.getItem("lista_compras")) || [];

  receita.lista.forEach(ingrediente => {
    lista.push({ nomeReceita: receita.nome, ingrediente });
  });

  localStorage.setItem("lista_compras", JSON.stringify(lista));
  alert(`Ingredientes da receita "${receita.nome}" adicionados à lista de compras!`);
}
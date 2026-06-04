const API_URL = "http://127.0.0.1:8000";

async function tratarResposta(response) {
    if (!response.ok) {
        const erroData = await response.json();
        throw new Error(erroData.detail || "Erro desconhecido na requisição.");
    }
    return await response.json();
}

// 1. FORMULÁRIO DE USUÁRIO
document.getElementById("userForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const msg = document.getElementById("userMsg");
    msg.style.color = "#3b82f6";
    msg.textContent = "Processando...";

    try {
        const res = await fetch(`${API_URL}/users`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: document.getElementById("nome").value,
                email: document.getElementById("email").value
            })
        });
        const usuario = await tratarResposta(res);
        msg.style.color = "#10b981";
        msg.textContent = `Sucesso! Usuário criado com ID: ${usuario.id}`;
        document.getElementById("userForm").reset();
    } catch (err) {
        msg.style.color = "#ef4444";
        msg.textContent = err.message;
    }
});

// 2. FORMULÁRIO DE CATEGORIA
document.getElementById("categoryForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const msg = document.getElementById("categoryMsg");
    msg.style.color = "#3b82f6";
    msg.textContent = "Processando...";

    try {
        const res = await fetch(`${API_URL}/categories`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                user_id: parseInt(document.getElementById("catUserId").value),
                name: document.getElementById("catNome").value
            })
        });
        const categoria = await tratarResposta(res);
        msg.style.color = "#10b981";
        msg.textContent = `Sucesso! Categoria ID: ${categoria.id} criada.`;
        document.getElementById("categoryForm").reset();
    } catch (err) {
        msg.style.color = "#ef4444";
        msg.textContent = err.message;
    }
});

// 3. FORMULÁRIO DE TAREFA
document.getElementById("taskForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const msg = document.getElementById("taskMsg");
    msg.style.color = "#3b82f6";
    msg.textContent = "Processando...";

    const catIdVal = document.getElementById("taskCatId").value;

    try {
        const res = await fetch(`${API_URL}/tasks`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                user_id: parseInt(document.getElementById("taskUserId").value),
                category_id: catIdVal ? parseInt(catIdVal) : null,
                title: document.getElementById("taskTitulo").value,
                description: document.getElementById("taskDesc").value,
                priority: document.getElementById("taskPrioridade").value,
                status: "Pendente"
            })
        });
        await tratarResposta(res);
        msg.style.color = "#10b981";
        msg.textContent = "Tarefa adicionada com sucesso!";
        document.getElementById("taskForm").reset();
        
        const buscaId = document.getElementById("buscaUserId").value;
        if(buscaId) buscarTarefasDoUsuario();
    } catch (err) {
        msg.style.color = "#ef4444";
        msg.textContent = err.message;
    }
});

// 4. BUSCA DE TAREFAS
async function buscarTarefasDoUsuario() {
    const userId = document.getElementById("buscaUserId").value;
    const listaContainer = document.getElementById("listaTarefas");

    if (!userId) {
        alert("Por favor, informe o ID do usuário para realizar a busca.");
        return;
    }

    listaContainer.innerHTML = "<p style='color: #64748b; font-style: italic;'>Consultando banco de dados MySQL...</p>";

    try {
        const res = await fetch(`${API_URL}/users/${userId}/tasks`);
        if (!res.ok) throw new Error("Não foi possível carregar as tarefas deste usuário.");
        
        const tarefas = await res.json();
        listaContainer.innerHTML = "";

        if (tarefas.length === 0) {
            listaContainer.innerHTML = "<p style='color: #64748b; font-style: italic;'>Nenhuma tarefa encontrada para este usuário no banco.</p>";
            return;
        }

        tarefas.forEach(tarefa => {
            const div = document.createElement("div");
            div.className = `task-card ${tarefa.status}`;
            div.innerHTML = `
                <div class="task-info">
                    <h4>${tarefa.title}</h4>
                    <p>${tarefa.description || 'Sem payload descritivo.'}</p>
                </div>
                <div class="task-badge">
                    ${tarefa.priority} | ${tarefa.status}
                </div>
            `;
            listaContainer.appendChild(div);
        });

    } catch (err) {
        listaContainer.innerHTML = `<p style="color: #ef4444; font-weight: 500;">Erro: ${err.message}</p>`;
    }
}
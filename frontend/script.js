const API_URL = "http://127.0.0.1:8000/api/instruments/";
const instrumentList = document.getElementById("instrument-list");
const instrumentForm = document.getElementById("instrument-form");
const modal = document.getElementById("modal");
const modalDetails = document.getElementById("modal-details");
const closeModal = document.querySelector(".close");

// Carregar instrumentos ao iniciar
document.addEventListener("DOMContentLoaded", fetchInstruments);

// Cadastrar novo instrumento
instrumentForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const newInstrument = {
        name: document.getElementById("name").value,
        category: document.getElementById("category").value,
        price: parseFloat(document.getElementById("price").value),
        description: document.getElementById("description").value,
    };

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newInstrument),
    });

    instrumentForm.reset();
    fetchInstruments();
});

// Listar todos os instrumentos
async function fetchInstruments() {
    const response = await fetch(API_URL);
    const instruments = await response.json();
    instrumentList.innerHTML = instruments.map(instrument => `
        <div class="instrument-item">
            <h3>${instrument.name}</h3>
            <div class="actions">
                <button class="view-btn" onclick="viewInstrument(${instrument.id})">Ver</button>
                <button class="delete-btn" onclick="deleteInstrument(${instrument.id})">Deletar</button>
            </div>
        </div>
    `).join("");
}

// Tornar as funções globais para que o HTML possa acessá-las
window.viewInstrument = async function (id) {
    const response = await fetch(`${API_URL}${id}/`);
    const instrument = await response.json();

    modalDetails.innerHTML = `
        <p><strong>Nome:</strong> ${instrument.name}</p>
        <p><strong>Categoria:</strong> ${instrument.category}</p>
        <p><strong>Preço:</strong> R$ ${parseFloat(instrument.price).toFixed(2)}</p>
        <p><strong>Descrição:</strong> ${instrument.description}</p>
    `;

    modal.style.display = "flex";
};

window.deleteInstrument = async function (id) {
    if (confirm("Tem certeza que deseja deletar este instrumento?")) {
        await fetch(`${API_URL}${id}/`, { method: "DELETE" });
        fetchInstruments();
    }
};

// Fechar modal
closeModal.addEventListener("click", () => {
    modal.style.display = "none";
});

window.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});

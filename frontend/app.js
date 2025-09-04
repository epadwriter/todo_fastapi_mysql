// Dirección del backend (cambiar al dominio real si lo despliegas)
const API_URL = "http://127.0.0.1:8000";

// 1. Obtener todas las tareas
async function cargarTareas() {
  const res = await fetch(API_URL + "/tareas");
  const data = await res.json();

  const lista = document.getElementById("lista");
  lista.innerHTML = "";
  data.forEach((t) => {
    lista.innerHTML += `
      <li>
        ${t.descripcion} 
        <button onclick="borrarTarea(${t.id})">❌</button>
      </li>`;
  });
}

// 2. Agregar nueva tarea
async function agregarTarea() {
  const input = document.getElementById("nuevaTarea");
  const tarea = input.value;

  if (tarea) {
    await fetch(API_URL + "/tareas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ descripcion: tarea })
    });

    input.value = "";
    cargarTareas();
  }
}

// 3. Borrar tarea
async function borrarTarea(id) {
  await fetch(API_URL + "/tareas/" + id, { method: "DELETE" });
  cargarTareas();
}

// 4. Cargar lista al abrir
cargarTareas();

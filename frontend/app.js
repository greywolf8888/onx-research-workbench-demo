async function loadCandidates() {
  const response = await fetch("/api/candidates");
  if (!response.ok) {
    throw new Error("Failed to load demo candidates");
  }
  return response.json();
}

function renderCandidates(payload) {
  const table = document.querySelector("#candidates");
  const summary = document.querySelector("#summary");
  table.innerHTML = "";
  payload.candidates.forEach((item) => {
    const row = document.createElement("div");
    row.className = "row";
    row.innerHTML = `
      <strong>${item.symbol}</strong>
      <span class="score">${item.score.toFixed(1)}</span>
      <span>${item.risk}</span>
    `;
    table.appendChild(row);
  });
  summary.innerHTML = `
    <strong>${payload.candidates.length} synthetic candidates</strong>
    <span class="muted">Generated at ${payload.generated_at}</span>
    <span class="muted">Source: ${payload.source}</span>
  `;
}

loadCandidates()
  .then(renderCandidates)
  .catch((error) => {
    document.querySelector("#candidates").textContent = error.message;
  });

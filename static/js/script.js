// Scripts home.html
// ========================================================================

function fecharAlerta(alertaId) {
    document.getElementById(alertaId).style.display = "none";
}
    
// Pega o parâmetro da URL
const urlParams = new URLSearchParams(window.location.search);
const sucesso = urlParams.get('sucesso');
const erro = urlParams.get('erro');
    
// Se o parâmetro for erro de data inválida, exibe o alerta de erro
if (erro === 'data_invalida') {
    document.getElementById("alertaErro").style.display = "block";
}
    
// Se o parâmetro for sucesso, exibe o alerta de sucesso
if (sucesso === 'true') {
    document.getElementById("alertaSucesso").style.display = "block";
}

// Final dos Scripts home.html
// ========================================================================

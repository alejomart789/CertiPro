$(document).ready(function() {
    // Escuchamos el evento "change" del switch
    $("#switchActualizacion").change(function() {
        // Enviamos el formulario automáticamente cuando cambia el estado del switch
        $("#actualizacionForm").submit();
    });
});

$(document).ready(function() {
    // Cuando se hace clic en el botón de edición (lapiz)
    $(".btn-editar-pregunta").on("click", function() {
        // Obtener la pregunta actual desde los atributos de datos del botón
        var preguntaId = $(this).data("pregunta-id");
        var preguntaTexto = $(this).data("pregunta-texto");
        var preguntaTipo = $(this).data("pregunta-tipo");

        // Rellenar el formulario con los datos de la pregunta
        $("#preguntaId").val(preguntaId);
        $("#preguntaTipo").val(preguntaTipo);
        $("#pregunta").val(preguntaTexto);

        // Establecer la acción del formulario para editar la pregunta con el ID correspondiente
        $("#formEditarPregunta").attr("action", "{% url 'tu_app:editar_pregunta' 0 %}".replace("0", preguntaId));

        // Mostrar el modal
        $("#modalEditarPregunta").modal("show");
    });
});

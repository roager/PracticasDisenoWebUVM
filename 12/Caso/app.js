$(document).ready(function() {
    // Login
    $('#login-form').submit(function(event) {
        event.preventDefault();
        const username = $('#username').val();
        const password = $('#password').val();

        // Verificar usuario contra la API
        $.ajax({
            url: 'http://127.0.0.1:8080/login',  // Cambié el puerto a 8080
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ usuario: username, password: password }),  // Enviar datos como JSON
            success: function(response) {
                localStorage.setItem('token', response.token);  // Guardar token de sesión
                $('#login-form').hide();
                $('#register-form').hide();
                $('#welcome-message').show();
            },
            error: function() {
                alert('Credenciales inválidas');
            }
        });
    });

    // Registro de nuevos usuarios
    $('#register-form').submit(function(event) {
        event.preventDefault();
        const username = $('#new-username').val();
        const password = $('#new-password').val();
        const age = $('#age').val();

        // Realizar una petición POST para registrar al nuevo usuario
        $.ajax({
            url: 'http://127.0.0.1:8080/register',  // Cambié el puerto a 8080
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ usuario: username, password: password, age: age }),  // Enviar datos como JSON
            success: function(response) {
                alert('Usuario registrado exitosamente');
            },
            error: function() {
                alert('Error al registrar el usuario');
            }
        });
    });

    // Obtener datos (GET)
    $('#get-data').click(function() {
        const token = localStorage.getItem('token');
        $.ajax({
            url: 'https://jsonplaceholder.typicode.com/users',
            type: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            success: function(response) {
                console.log(response);  // Mostrar usuarios obtenidos
                alert('Datos obtenidos correctamente');
            },
            error: function() {
                alert('Error al obtener datos');
            }
        });
    });

    // Enviar datos (POST)
    $('#post-data').click(function() {
        const token = localStorage.getItem('token');
        $.ajax({
            url: 'https://jsonplaceholder.typicode.com/posts',
            type: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            data: JSON.stringify({
                title: 'foo',
                body: 'bar',
                userId: 1
            }),
            contentType: 'application/json',
            success: function(response) {
                console.log(response);  // Mostrar datos enviados
                alert('Datos enviados correctamente');
            },
            error: function() {
                alert('Error al enviar datos');
            }
        });
    });
});

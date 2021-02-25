from django.test import TestCase

# Create your tests here.

  <title>Авторизируйтесь</title>

  <link
    rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
    integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4"
    crossorigin="anonymous">
</head>
<body>
  <div class="jumbotron">
    <h1>Авторизируйтесь!</h1>
    {% if user.is_authenticated %}
      <p>Logged as {{ user.username }}</p>
      <a class="btn btn-primary" href="{% url 'log_out' %}">Logout</a>
    {% else %}
      <a class="btn btn-primary" href="{% url 'social:begin' 'google-oauth2' %}">
        Login
      </a>
    {% endif %}
  </div>
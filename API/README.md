# APIs

> **warning** Necesitas cargo: https://doc.rust-lang.org/cargo/getting-started/installation.html 

## ¿Qué es una Web API?

En términos simples, una Web API (Interfaz de Programación de Aplicaciones en la Web) actúa como un medio estandarizado para que diferentes aplicaciones se comuniquen a través de la red. Imagina un puente digital que facilita el intercambio de información y funcionalidades entre sistemas diversos.

## Importancia de las Web API

- `Interconexión Eficiente`: Permiten la integración fluida de servicios y aplicaciones, optimizando la comunicación entre distintos componentes.
- `Reutilización de Funcionalidades`: Al exponer funciones específicas, las Web API posibilitan que otros desarrolladores las utilicen sin profundizar en la complejidad interna de la aplicación original.
- `Escalabilidad`: Facilitan el desarrollo de aplicaciones al permitir que diferentes partes operen de manera independiente, favoreciendo la flexibilidad y el crecimiento.

## Getting Started

### Creación del entorno virtual

> **Nota:** Para poder ejecutar los comandos de este documento es necesario tener instalado [virtualenv](https://virtualenv.pypa.io/en/latest/).
> `pip install virtualenv`

1. Crea el entorno virtual:

```bash
virtualenv example-api
```

2. Activa el entorno virtual:

En linux:

```bash
source example-api/bin/activate
```

En Windows:

```bash
.\example-api\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

Si queremos crear un nuevo archivo de dependencias:

```bash
pip freeze > requirements.txt
```

4. Ejecuta el servidor:

```bash
uvicorn main:app --reload
```

5. Abre el navegador en la siguiente dirección: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

6. Para desactivar el entorno virtual:

```bash
deactivate
```

### Documentación

- [Swagger](http://127.0.0.1:8000/docs)
- [Redoc](http://127.0.0.1:8000/redoc)

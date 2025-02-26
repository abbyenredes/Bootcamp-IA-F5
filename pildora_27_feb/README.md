# Vamos a crear nuestros propios test unitarios y de integración

## Acerca del proyecto
Vamos a crear test que nos ayuden a pulir y optimizar nuestro código.

### Mis herramientas
* Ciclo de vida del software con efoque ágil: [desarrolo de software](https://www.canvia.com/ciclo-vida-desarrollo-software/)
* Desarrollo de software paso a paso: [desarrolla paso a paso](https://www.red-tic.unam.mx/desarrollo-de-software)
* Claves de un buen testing: [Testing](https://www.linkedin.com/pulse/por-qu%C3%A9-el-testing-es-clave-en-desarrollo-de-software-cristian/)
* ¿Por qué? buenas practicas: [puebas unitarias](https://yeeply.com/blog/tendencias-habilidades/que-son-pruebas-unitarias/)
* Diferencia entre test unitarios y de integración: [test unitarios vs test integracion](https://hackernoon.com/lang/es/la-diferencia-entre-pruebas-unitarias-y-pruebas-de-integraci%C3%B3n)
* Tipos de test en python: [herramientas de test](https://openwebinars.net/blog/herramientas-de-testing-en-python/)
* Documentación de Unittest: [documentación Unittest](https://docs.python.org/3/library/unittest.html)


## Comparación entre Pruebas Unitarias y Pruebas de Integración

| **Característica**        | **Pruebas Unitarias**                                                                                   | **Pruebas de Integración**                                                                 |
|---------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Definición**            | Validan un componente individual del software, como una función o método.                            | Verifican la interacción entre múltiples componentes y su integración con el entorno.     |
| **Objetivo**              | Asegurar que cada unidad funcione correctamente de manera aislada.                                   | Garantizar que los módulos trabajen juntos sin errores.                                   |
| **Alcance**               | Se enfocan en una única unidad de código.                                                            | Involucran múltiples módulos y sus interacciones.                                         |
| **Automatización**        | Altamente automatizables, facilitando pruebas de regresión.                                         | Pueden ser automatizadas, pero requieren configuraciones más complejas.                   |
| **Uso de dependencias**   | Se usan mocks o stubs para simular dependencias externas.                                           | Requieren conexión con bases de datos, APIs u otros sistemas externos.                    |
| **Complejidad**           | Baja, son simples de escribir y ejecutar.                                                           | Mayor, ya que incluyen múltiples componentes y su configuración.                          |
| **Velocidad de ejecución**| Rápidas, debido a la falta de dependencias externas.                                               | Más lentas, ya que dependen de la interacción entre módulos y recursos externos.          |
| **Cuándo aplicarlas**     | Durante el desarrollo, antes de la integración del sistema completo.                               | Después de las pruebas unitarias, al integrar los componentes del sistema.                |


## Comparativa de Herramientas de Testing en Python

| **Herramienta**     | **Tipo de Prueba**              | **Pros** | **Contras** |
|---------------------|--------------------------------|----------|-------------|
| **unittest**       | Unitarias                      | Incluido en la biblioteca estándar. <br> Amplia documentación y comunidad. | Sintaxis más detallada que otras herramientas. |
| **pytest**         | Unitarias e integración        | Sintaxis sencilla y fácil de usar. <br> Soporte para fixtures y plugins. | Requiere instalación adicional. |
| **nose2**          | Unitarias e integración        | Extiende funcionalidades de unittest. <br> Soporte para plugins. | Menos popular que unittest y pytest. |
| **doctest**        | Unitarias                      | Permite escribir pruebas en docstrings. <br> Fácil de usar en pequeños módulos. | Menos adecuado para pruebas complejas. |
| **Hypothesis**     | Pruebas basadas en propiedades | Genera datos de prueba automáticamente. <br> Detecta casos límite inesperados. | Puede ser más complejo de configurar. |
| **Schemathesis**   | Pruebas de API                 | Pruebas automáticas para APIs OpenAPI/Swagger. <br> Detecta errores de contrato. | Requiere documentación OpenAPI bien definida. |
| **Playwright**     | Pruebas de UI/E2E              | Soporta múltiples navegadores. <br> Rápido y confiable para pruebas front-end. | Puede ser más complejo de configurar en proyectos grandes. |
| **Robot Framework**| Pruebas de aceptación/E2E      | Sintaxis basada en palabras clave fácil de leer. <br> Soporte para Selenium, API y más. | Menos flexible para pruebas unitarias. |
| **Locust**         | Pruebas de carga               | Pruebas de rendimiento con Python. <br> Fácil de escalar y simular miles de usuarios. | No adecuado para pruebas funcionales o unitarias. |


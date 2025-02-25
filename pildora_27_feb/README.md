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

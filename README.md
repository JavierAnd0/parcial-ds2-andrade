En el README.md, identifiquen el nombre de la base de datos, sus tres colecciones, los campos
de cada documento con su tipo de dato y cómo se relacionan (qué campo usan como
referencia).

Nombre base de datos = matriculapp
colleciones: Agente
             Semana
             tickets

Campos con tipo de dato
=== agentes (2 documentos)
  _id: objectId
  nombre: string
  nivel: string
  ticketsPorHora: int
  enTurno: bool
  Ejemplo:
{
  nombre: 'Laura Cerquera',
  nivel: 'Senior',
  ticketsPorHora: 10,
  enTurno: true
}

=== tickets (8 documentos)
  _id: string
  llegada: int
  atencion: int
  prioridad: string
  Ejemplo:
{
  llegada: 0,
  atencion: 5,
  prioridad: 'Alta'
}

=== semana (8 documentos)
  _id: objectId
  numeroSemana: int
  numeroDefectos: int
  Ejemplo:
{
  numeroSemana: 1,
  numeroDefectos: 28
}

Interpretacion

Pregunta: ¿cuántos defectos quedarían sin descubrir si se libera hoy? ¿En qué semana se
llegaría al 95 % (t = ln 20 / b)


• Prueba sugerida: goel(0, a, b) debe valer 0

Pregunta
Con los datos de las semanas de prueba que se dieron en la tabla y despues de realizado el modelo, se puede concluir que segun el modelo Goel matriculapp tiene 198 defectos, hasta la semana 8 se encontraron 139 defectos, por lo que en caso de liberarse "hoy" quedarian 59 defectos sin descubrir, Para llegar al 95% tendria que probar hasta la semana 20, por lo que NO se recomienda liberar la version, todavia tiene un gran porcentaje de error faltante. 
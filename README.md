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


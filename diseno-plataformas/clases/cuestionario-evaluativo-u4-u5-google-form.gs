/**
 * Crea en Google Forms el cuestionario evaluativo de las Unidades 4 y 5
 * (mismo contenido que cuestionario-evaluativo-u4-u5.md).
 *
 * Uso:
 *   1. Abrir https://script.google.com con la cuenta de la cátedra → Nuevo proyecto.
 *   2. Borrar el contenido de Código.gs y pegar este archivo completo.
 *   3. Elegir la función crearCuestionario y tocar Ejecutar. Autorizar el acceso a Forms.
 *   4. En "Registro de ejecución" aparecen los enlaces para editar y para responder.
 *
 * Puntaje (total 100):
 *   A. Opción múltiple: 8 × 4, corrección automática.
 *   B. Verdadero o falso: 7 × (2 automáticos por V/F + 2 manuales por la justificación).
 *   C. Respuesta corta: 5 × 8, corrección manual.
 *
 * Las preguntas 9 y 10 son verdaderas: quien marque "Verdadero" no tiene que justificar,
 * así que la docente le asigna a mano los 2 puntos de la justificación (pestaña Respuestas → Individual).
 * Todas las preguntas V/F tienen campo de justificación para no delatar cuáles son falsas.
 */

function crearCuestionario() {
  var form = FormApp.create('Cuestionario evaluativo — Unidades 4 y 5');
  form.setIsQuiz(true);
  form.setDescription(
    'Diseño según Plataformas de Juego · FI – UNJu · 2026\n' +
    'Unidad 4: Plataforma móvil · Unidad 5: Consolas · Laboratorio de adaptación ' +
    '(Asteroides y 2D Platformer en PC, Android y Xbox)\n\n' +
    'Instrucciones\n' +
    '• 20 preguntas en tres partes. Duración sugerida: 60 minutos.\n' +
    '• Parte A: marcá una sola opción.\n' +
    '• Parte B: marcá V o F. Si es falsa, justificá en una línea; sin justificación, la respuesta vale la mitad.\n' +
    '• Parte C: respondé en 3 a 5 líneas.\n\n' +
    'Puntaje: A. Opción múltiple (1 a 8) 8 × 4 = 32 · B. Verdadero o falso (9 a 15) 7 × 4 = 28 · ' +
    'C. Respuesta corta (16 a 20) 5 × 8 = 40 · Total 100'
  );

  form.addTextItem().setTitle('Nombre y apellido').setRequired(true);
  form.addTextItem().setTitle('LU').setRequired(true);

  // ---------- Parte A ----------
  form.addPageBreakItem().setTitle('Parte A — Opción múltiple')
    .setHelpText('Marcá una sola opción. 4 puntos cada una.');

  opcionMultiple(form,
    '1. Asteroides corre a 60 fps al empezar en un teléfono, pero a los 8 minutos baja a 35–40 fps. ' +
    'En el Editor de la PC marcaba 200 fps. ¿Cuál es la explicación más probable?',
    [
      'a) El Editor mide mal los fps y el teléfono siempre estuvo a 40.',
      'b) El teléfono se calienta, el SoC baja sus relojes (throttling) y cae el rendimiento sostenido.',
      'c) Unity móvil limita el juego a 30 fps desde el primer minuto.',
      'd) El juego tiene un error de lógica que aparece después de 8 minutos.'
    ], 1,
    'Pico vs. sostenido: calor → throttling → caen los fps. Importa el minuto 10, no el 1. ' +
    'El número del Editor no predice el del teléfono.');

  opcionMultiple(form,
    '2. En los Player Settings de Android de Asteroides, la opción ARM64 aparece en gris y no se puede ' +
    'tildar. ¿Por qué?',
    [
      'a) Porque el Minimum API Level es demasiado bajo.',
      'b) Porque está tildado "Build App Bundle".',
      'c) Porque el Scripting Backend es Mono; ARM64 se habilita solo con IL2CPP.',
      'd) Porque Active Input Handling está en "Both".'
    ], 2,
    'Según la documentación de Unity 6.3, ARM64 se habilita solo cuando el Scripting Backend es IL2CPP. ' +
    'El proyecto estaba en Mono + ARMv7.');

  opcionMultiple(form,
    '3. ¿Qué permite comprobar el Device Simulator de Unity?',
    [
      'a) El rendimiento y la temperatura del teléfono.',
      'b) El layout de la UI y la safe area en distintas pantallas.',
      'c) Mover y disparar con dos dedos a la vez.',
      'd) El consumo de memoria real del dispositivo.'
    ], 1,
    'El Device Simulator prueba layout y safe area; no prueba rendimiento, memoria ni temperatura, ' +
    'y simula un solo dedo.');

  opcionMultiple(form,
    '4. Sobre los documentos de Microsoft para Xbox, ¿cuál afirmación es correcta?',
    [
      'a) Los XR (Xbox Requirements) son obligatorios para certificar; las XAG (accesibilidad) son ' +
        'recomendaciones de buenas prácticas.',
      'b) Las XAG son obligatorias y los XR son opcionales.',
      'c) Cumplir todas las XAG garantiza la certificación.',
      'd) Los XR y las XAG son el mismo documento con dos nombres.'
    ], 0,
    'XR = condición para publicar. XAG = buenas prácticas, no pensadas como lista de control.');

  opcionMultiple(form,
    '5. El requisito XR-130 pide los mismos modos de juego en todos los modelos de una generación ' +
    '(por ejemplo, Series S y Series X). ¿Qué consecuencia tiene para el diseño?',
    [
      'a) Hay que publicar dos juegos distintos, uno por modelo.',
      'b) El modelo más débil (Series S, 10 GB) fija el piso de lo que el juego puede ofrecer.',
      'c) La Series X puede tener modos de juego exclusivos.',
      'd) Ninguna: solo afecta a la tienda.'
    ], 1,
    'Mismos modos en toda la generación: el modelo más débil manda (caso Baldur\'s Gate 3 en Series S).');

  opcionMultiple(form,
    '6. ¿Qué vía se usó en la cátedra para llevar Asteroides y el Platformer a una Xbox Series X?',
    [
      'a) GDK con el programa ID@Xbox y un kit de desarrollo.',
      'b) Publicación en la Microsoft Store.',
      'c) Developer Mode en la consola y un paquete UWP (.msix) instalado desde el Device Portal por la ' +
        'red local.',
      'd) Streaming del juego desde la PC con Xbox Cloud Gaming.'
    ], 2,
    'Developer Mode + UWP: cuenta gratuita de Partner Center y .msix por Device Portal. ' +
    'Sirve para probar, no para publicar.');

  opcionMultiple(form,
    '7. En la primera corrida de los tests de Asteroides de consola, 5 tests fallaron porque el juego se ' +
    'pausaba solo al cargar la escena. ¿Cuál era la causa?',
    [
      'a) El mando de Xbox no estaba conectado a la PC durante los tests.',
      'b) Al ocultar el joystick táctil fuera del móvil, se quitaba su gamepad virtual y la capa de ' +
        'consola lo interpretaba como un mando desconectado.',
      'c) Ship.cs llamaba a la pausa en cada frame.',
      'd) Unity no soporta tests de Play Mode en proyectos UWP.'
    ], 1,
    'Al apagarse, OnScreenStick y OnScreenButton quitan su gamepad virtual y la capa pausaba. ' +
    'Corrección: solo cuentan los mandos físicos (device.native).');

  opcionMultiple(form,
    '8. Al portear el 2D Platformer a Android, dos tests de Play Mode fallaron ' +
    '(GroundRay_InMidAir_HitsNothing y SecondJumpIntent_InAir_DoubleJumpsOnlyOnce). ¿Qué revelaron?',
    [
      'a) Que los botones táctiles ◀ ▶ no funcionaban.',
      'b) Que el porteo había roto el salto.',
      'c) Un defecto del juego original: el rayo de IsGrounded() golpeaba el collider del propio ' +
        'jugador, por eso el salto era infinito.',
      'd) Que el Input System no lee el botón Sur del gamepad.'
    ], 2,
    'El rayo nacía dentro del CapsuleCollider2D del jugador e IsGrounded() siempre era verdadero. ' +
    'Era un defecto del original, no del porteo.');

  // ---------- Parte B ----------
  form.addPageBreakItem().setTitle('Parte B — Verdadero o falso')
    .setHelpText('Marcá V o F (2 puntos). Si es falsa, justificá en una línea (2 puntos).');

  verdaderoFalso(form,
    '9. En el porteo de Asteroides a Android, Ship.cs dejó de leer Input.GetKey y pasó a recibir la ' +
    'intención con SetIntent(mover, disparar); los métodos MoveLeft, MoveRight y ShootLaser no cambiaron.',
    true, '');

  verdaderoFalso(form,
    '10. Los controles en pantalla (OnScreenStick y OnScreenButton) simulan un gamepad virtual; por eso ' +
    'el adaptador de entrada no distingue el dedo de un gamepad físico.',
    true, '');

  verdaderoFalso(form,
    '11. En Unity 6.3, Active Input Handling = "Both" está soportado oficialmente en Android, y por eso ' +
    'se usó también en el Platformer v2.',
    false,
    'Unity 6.3 declara "Both" no soportado en Android (aviso "Unsupported Input Handling on Android"). ' +
    'El Platformer v2 usó solo "Input System Package (New)".');

  verdaderoFalso(form,
    '12. Para adaptar Asteroides a la Xbox hubo que reescribir Ship.cs y modificar las escenas del juego.',
    false,
    'Se agregó una capa de consola que se instala sola al arrancar. No se tocaron escenas ni prefabs, ' +
    'y Ship.cs es el mismo.');

  verdaderoFalso(form,
    '13. Como los cuatro paquetes .msix (Asteroides y Platformer, original y consola) se generaron sin ' +
    'errores, queda demostrado que los cuatro juegos corren en la Xbox.',
    false,
    'Generar el paquete prueba que se compila y que declara la familia Xbox. Que corra en la consola ' +
    'solo lo demuestra la prueba en la Xbox.');

  verdaderoFalso(form,
    '14. Si un test queda en rojo después de un cambio, el cambio que acabamos de hacer es siempre la causa.',
    false,
    'En Asteroides, las 3 hipótesis del pool fallaban antes y después del porteo, y otra falla era ' +
    'inestable. Hay que leer el stack trace y comparar con la línea base.');

  verdaderoFalso(form,
    '15. Sony y Nintendo publican sus requisitos de certificación completos, igual que Microsoft con los XR.',
    false,
    'Solo Microsoft publica los XR y sus casos de prueba. Sony y Nintendo los tienen bajo NDA; ' +
    'solo publican los pasos de alta.');

  // ---------- Parte C ----------
  form.addPageBreakItem().setTitle('Parte C — Respuesta corta')
    .setHelpText('Respondé en 3 a 5 líneas. 8 puntos cada una.');

  respuestaCorta(form,
    '16. Explicá la diferencia entre dispositivo, intención y lógica del juego. Dá un ejemplo con ' +
    'Asteroides en PC (teclado), Android (táctil) y Xbox (mando).', '',
    'Dispositivo = cómo pide la acción el jugador; intención = qué quiere hacer; lógica = la nave, que ' +
    'no sabe de dónde vino la orden. Teclado, táctil y mando terminan en Ship.SetIntent(mover, disparar).');

  respuestaCorta(form,
    '17. Al poner Asteroides en orientación vertical, los asteroides nacen fuera de la pantalla. ' +
    'Explicá por qué, usando el ancho visible de la cámara y el rango donde aparecen los asteroides.', '',
    'La cámara ve 5 × aspect a cada lado: unas 8,9 unidades en 16:9 y unas 2,8 en vertical. ' +
    'Los asteroides aparecen en x ∈ [−8, 8], un rango pensado para horizontal.');

  respuestaCorta(form,
    '18. Nombrá tres cambios que la capa de consola agrega a Asteroides y al Platformer respecto de la ' +
    'versión original, y explicá por qué cada uno es necesario en una consola jugada desde el sillón.', '',
    'Foco visible (amarillo) y navegación con mando, pausa (Menu, mando desconectado, foco perdido), ' +
    'texto de al menos 26 px a 1080p, botón Salir oculto.');

  respuestaCorta(form,
    '19. La capa de consola pausa el juego por tres motivos. ¿Cuáles son? ¿Qué requisito o caso de ' +
    'prueba de Xbox se relaciona con uno de ellos?', '',
    'Botón Menu durante la partida, mando físico desconectado y pérdida de foco. La desconexión se ' +
    'relaciona con el XR-115 y su caso de prueba 115-02.');

  respuestaCorta(form,
    '20. Completá con el archivo instalable de cada plataforma y cómo se instala o se ejecuta.',
    'Respondé una línea por plataforma:\n' +
    'PC (Windows): archivo — cómo se instala o se ejecuta\n' +
    'Android: archivo — cómo se instala o se ejecuta\n' +
    'Xbox (Developer Mode): archivo — cómo se instala o se ejecuta',
    'PC: .exe e instalador (Inno Setup). Android: .apk, copiarlo y aceptar fuentes desconocidas o ' +
    'adb install -r. Xbox: .msix x64 con la dependencia VCLibs, instalado desde el Device Portal.');

  // Desde 2025 los formularios nuevos pueden quedar sin publicar; se publica si la API lo permite.
  if (typeof form.setPublished === 'function') {
    form.setPublished(true);
  }

  Logger.log('Editar: ' + form.getEditUrl());
  Logger.log('Responder: ' + form.getPublishedUrl());
}

function opcionMultiple(form, titulo, opciones, correcta, comentario) {
  var item = form.addMultipleChoiceItem();
  item.setTitle(titulo)
    .setPoints(4)
    .setRequired(true)
    .setChoices(opciones.map(function (texto, i) {
      return item.createChoice(texto, i === correcta);
    }))
    .setFeedbackForCorrect(FormApp.createFeedback().setText(comentario).build())
    .setFeedbackForIncorrect(FormApp.createFeedback().setText(comentario).build());
}

function verdaderoFalso(form, titulo, esVerdadera, justificacion) {
  var item = form.addMultipleChoiceItem();
  item.setTitle(titulo)
    .setPoints(2)
    .setRequired(true)
    .setChoices([
      item.createChoice('Verdadero', esVerdadera),
      item.createChoice('Falso', !esVerdadera)
    ]);
  if (justificacion) {
    item.setFeedbackForCorrect(FormApp.createFeedback().setText(justificacion).build())
      .setFeedbackForIncorrect(FormApp.createFeedback().setText(justificacion).build());
  }

  var just = form.addParagraphTextItem();
  just.setTitle('Justificación de la pregunta ' + titulo.split('.')[0] + ' (solo si marcaste Falso)')
    .setPoints(2)
    .setRequired(false);
  if (justificacion) {
    just.setGeneralFeedback(FormApp.createFeedback().setText(justificacion).build());
  }
}

function respuestaCorta(form, titulo, ayuda, comentario) {
  var item = form.addParagraphTextItem();
  item.setTitle(titulo)
    .setPoints(8)
    .setRequired(true)
    .setGeneralFeedback(FormApp.createFeedback().setText(comentario).build());
  if (ayuda) {
    item.setHelpText(ayuda);
  }
}

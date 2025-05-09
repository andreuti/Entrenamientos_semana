import streamlit as st

st.set_page_config(layout="wide")
st.title("📅 Rutina Semanal Funcional – Estabilidad, Rotación y Prevención")

dias = {
    "🏠🏋️Lunes": [
        "Dead bug con banda elástica",
        "Bird dog lento",
        "Puente de glúteos con elevación de pierna",
        "Pallof Press con goma",
        "Side plank con rodilla apoyada",
        "Clamshells lentos",
        "Desayunar",
        "Remo bajo en máquina con agarre en V",
        "Remo con cuerda en polea desde sentadilla parcial",
        "Elevación de torso en fitball",
        "Press Arnold",
        "Face pulls en polea con cuerda",
        "Golpe rotacional con balón medicinal contra pared",
        "Slam lateral con balón medicinal al suelo",
        "Golpe con balón medicinal sin lanzamiento + pausa",
        "Natación",
        "Estiramientos en sauna"
    ],
    "🏠🏃Martes": [
        "Dead bug con banda elástica",
        "Bird dog lento",
        "Pallof Press con goma",
        "Sentadilla isométrica con giro de tronco",
        "Clamshells lentos",
        "Rotaciones con palo de escoba",
        "Golpe con banda elástica con pausa",
        "Wall shadow con hombro fijo",
        "Golpe con balón medicinal sin lanzamiento + pausa",
        "Correr 5 km",
        "Estiramientos y foam roller"
    ],
    "🏠🏋️Miércoles": [
        "Dead bug con banda elástica",
        "Bird dog lento",
        "Puente de glúteos con elevación de pierna",
        "Pallof Press con goma",
        "Side plank con rodilla apoyada",
        "Clamshells lentos",
        "Desayunar",
        "Remo bajo en máquina con agarre en V",
        "Remo con cuerda en polea desde sentadilla parcial",
        "Elevación de torso en fitball",
        "Press Arnold",
        "Face pulls en polea con cuerda",
        "Golpe rotacional con balón medicinal contra pared",
        "Slam lateral con balón medicinal al suelo",
        "Golpe con balón medicinal sin lanzamiento + pausa",
        "Natación",
        "Estiramientos en sauna"
    ],
    "🏠🏃Jueves": [
        "Dead bug con banda elástica",
        "Bird dog lento",
        "Puente de glúteos con elevación de pierna",
        "Pallof Press con goma",
        "Side plank con rodilla apoyada",
        "Clamshells lentos",
        "Golpe rotacional con balón medicinal contra pared",
        "Slam lateral con balón medicinal al suelo",
        "Golpe con balón medicinal sin lanzamiento + pausa",
        "Correr 5 km",
        "Estiramientos y foam roller"
    ],
    "🏋️Viernes": [
        "Battlebox a las 14h (cardio, fuerza global y reacción)",
        "Natación",
        "Estiramientos en sauna"
    ],
    "🚲 Sábado": [
        "Bici (rodaje tranquilo o regenerativo)",
        "Estiramientos y foam roller",
        "Estiramientos activos de isquios y psoas",
        "Movilidad torácica suave (1-2 ejercicios)"
    ]
}
info_ejercicios = {
    "Dead bug con banda elástica": {
        "descripcion": """
        Mejora la estabilidad lumbopélvica y la coordinación contralateral.
        - Mantén la zona lumbar pegada al suelo durante todo el movimiento.
        - Mueve brazo y pierna opuestos al mismo tiempo, de forma lenta y controlada.
        - Si usas banda, añade tensión entre manos y pies para activar más el core.
        """,
        "imagen": ["img/Dead_bug_con_banda1.jpg","img/Dead_bug_con_banda2.jpg"]
    },
    "Bird dog lento": {
        "descripcion": """
        Refuerza el control de cadera y columna lumbar.
        - En cuadrupedia, extiende brazo y pierna contrarios lentamente.
        - Mantén pelvis estable, sin inclinaciones.
        - Realiza una pausa de 1-2 segundos en cada extensión.
        """,
        "imagen": "Bird_dog_lento.jpg"
    },
    "Puente de glúteos con elevación de pierna": {
        "descripcion": """
        Mejora activación de glúteos y control pélvico.
        - Eleva la pelvis con ambas piernas, luego estira una pierna sin que caiga la cadera.
        - Mantén el abdomen activado y controla el descenso.
        """,
        "imagen": "img/Puente_de_gluteo_con_elevacion_de_pierna.webp"
    },
    "Pallof Press con goma": {
        "descripcion": """
        Ejercicio antirrotacional para fortalecer el core profundo.
        - Coloca una banda elástica atada a un punto lateral.
        - Extiende los brazos al frente sin que el tronco gire.
        - Mantén la tensión durante 1-2 segundos y vuelve.
        """,
        "imagen": ["img/Pallof_press_con_goma1.jpg","img/Pallof_press_con_goma2.jpg"]
    },
    "Side plank con rodilla apoyada": {
        "descripcion": """
        Fortalece los oblicuos y estabilizadores laterales sin sobrecargar la lumbar.
        - Apoya el antebrazo y la rodilla más cercana al suelo.
        - Eleva la cadera y mantén la línea recta desde hombros a rodilla.
        - Progresión: eleva la pierna libre.
        """,
        "imagen": "img/side_plank_con_rodilla_apoyada.jpg"
    },
    "Clamshells lentos": {
        "descripcion": """
        Activa el glúteo medio, clave para estabilizar cadera y proteger la zona lumbar.
        - Túmbate de lado con las rodillas flexionadas.
        - Abre la rodilla superior sin separar los pies.
        - Movimiento lento, sin balancear la pelvis.
        - Se puede hacer mejor estando en plancha lateral
        """,
        "imagen": ["img/Clamshell_con_banda1.jpg", "img/Clamshell_con_banda2.jpg"]
    },
    "Rotaciones con palo de escoba": {
        "descripcion": """
        Entrena la movilidad torácica y la disociación cadera-tronco.
        - Mantén los pies fijos y gira solo el tronco.
        - Controla la vuelta, evitando impulso.
        - Ideal para aprender a 'guardar la cadera' mientras el tronco gira.
        """,
        "imagen": "img/rotacion_de_troncoo_con_palo.jpg"
    },
    "Sentadilla isométrica con giro de tronco": {
        "descripcion": """
        Refuerza el core en posición baja y mejora el control postural rotacional.
        - Apóyate en pared en posición de sentadilla (90º).
        - Gira los brazos lentamente de lado a lado sin perder altura.
        """,
        "imagen": None,
        "video": "https://www.youtube.com/watch?v=cZSMJJI8_YY"
    }
}


info_ejercicios.update({
    "Golpe con banda elástica con pausa": {
        "descripcion": """
        Reprograma la secuencia correcta de golpeo: cadera → tronco → brazo.
        - Sujeta la goma a la altura del pecho y simula el gesto de derecha o revés.
        - Haz el gesto lento y PAUSA en el momento de impacto imaginario.
        - Mantén la cadera semi-rotada y el pecho apuntando al frente.
        - Luego completa el golpe soltando la energía acumulada.
        """,
        "imagen": None
    },
    "Wall shadow con hombro fijo": {
        "descripcion": """
        Mejora la estabilidad del hombro adelantado y la conciencia del eje corporal.
        - Colócate de lado frente a una pared, con raqueta o palo.
        - Haz el gesto de golpeo y frena justo antes del impacto.
        - El hombro adelantado debe seguir apuntando hacia la pared.
        """,
        "imagen": None
    },
    "Golpe con balón medicinal sin lanzamiento + pausa": {
        "descripcion": """
        Refuerza el control de la rotación sin soltar la energía.
        - Sujeta el balón frente al pecho en posición de golpe.
        - Gira el tronco sin mover los pies y PAUSA cuando el pecho aún esté cerrado.
        - Luego puedes soltar el movimiento o reiniciar.
        """,
        "imagen": None
    },
    "Golpe rotacional con balón medicinal contra pared": {
        "descripcion": """
        Entrena la rotación potente con transferencia de peso.
        - Lanza el balón contra la pared como si fuera una derecha o revés.
        - Usa las piernas para empujar y rota desde el core.
        - El brazo debe seguir al tronco, no ir solo.
        """,
        "imagen": None,
        "video": "https://www.youtube.com/watch?v=PNI1QKiWfiY"
    },
    "Slam lateral con balón medicinal al suelo": {
        "descripcion": """
        Desarrolla potencia rotacional controlada y trabajo del core oblicuo.
        - Desde posición atlética, gira el cuerpo y lanza el balón al suelo al lado.
        - Evita girar los pies: rota desde el tronco.
        - Mantén hombros abajo y abdominales activos.
        """,
        "imagen": None,
        "video": "https://www.youtube.com/watch?v=wrBeL_-Dxzw"
    }
})


info_ejercicios.update({
    "Remo bajo en máquina con agarre en V": {
        "descripcion": """
        Fortalece la espalda media y estabiliza los omóplatos.
        - Siéntate erguido, agarre neutro en V.
        - Tira hacia el ombligo sin encoger los hombros.
        - Controla la vuelta, mantén el pecho proyectado.
        """,
        "imagen": "img/Remo_bajo_en_maquina_con_agarre_en_V.png"
    },
    "Remo desde sentadilla parcial": {
        "descripcion": """
        Integra fuerza postural con activación de dorsal ancho.
        - Colócate en una sentadilla parcial y **mantén la posición durante todo el ejercicio** (cadera hacia atrás, espalda recta, piernas flexionadas).
        - Tira de la cuerda hacia la cara o el pecho sin perder el eje corporal.
        - Controla la postura lumbar en todo momento, evitando encorvar la espalda.
        - Ideal para fortalecer desde una base estable y conectar tronco-brazo sin extensión de piernas.
        """,
        "imagen": None
    },
    "Elevación de torso en fitball": {
        "descripcion": """
        Refuerza la musculatura extensora lumbar de forma controlada.
        - Apoya el abdomen sobre el fitball, pies fijos.
        - Sube el torso activando glúteos y espalda baja, sin arquear en exceso.
        - Movimiento lento y con pausa arriba.
        """,
        "imagen": None,
        "video": "https://www.youtube.com/watch?v=zyBowrSR6pI"
    },
    "Press Arnold": {
        "descripcion": """
        Fortalece deltoides y mejora la movilidad de hombro.
        - Comienza con mancuernas al frente, palmas mirando al cuerpo.
        - Gira al subir hasta acabar con palmas hacia fuera.
        - Evita arquear la espalda. Usa peso controlado.
        """,
        "imagen": "img/PRESS_ARNOLD.png"
    },
    "Face pulls en polea con cuerda": {
        "descripcion": """
        Clave para fortalecer la musculatura posterior del hombro y mejorar la postura.
        - Altura de cuerda: nivel de la cara.
        - Tira separando manos y llevando la cuerda hacia la frente.
        - Aprieta omóplatos sin elevar los hombros.
        """,
        "imagen": "img/face_pulls.jpg"
    }
})

info_ejercicios.update({
    "Estiramientos y foam roller": {
        "descripcion": """
        Descarga muscular general y movilidad miofascial posterior a entrenamientos exigentes.

        🔹 Foam Roller (orden recomendado):
        1. **Isquiotibiales**: siéntate sobre el suelo, coloca el rodillo debajo de los muslos y rueda desde el glúteo hasta detrás de la rodilla.
        2. **Cuádriceps**: en posición de plancha, apoya un muslo sobre el rodillo y rueda desde la cadera hasta la rodilla.
        3. **Glúteos**: siéntate sobre el rodillo y cruza una pierna sobre la otra, gira ligeramente hacia ese lado.
        4. **Dorsales y espalda media**: apóyate boca arriba y rueda suavemente desde debajo de los omóplatos hasta el centro de la espalda.

        🔹 Estiramientos:
        - Mantén cada posición entre 20–40 segundos.
        - Acompaña con respiración nasal y controlada.
        """,
        "imagen": None
    },
    "Estiramientos activos de isquios y psoas": {
        "descripcion": """
        Estiramientos dinámicos que mejoran la flexibilidad funcional de la cadera.

        🔸 **Psoas (estocada dinámica):**
        - Coloca una pierna al frente y la otra atrás (rodilla en el suelo).
        - Retroversión pélvica (mete culete).
        - Eleva los brazos y desplaza el tronco ligeramente hacia delante.
        - Mantén 3–5 segundos y vuelve. Repite 8–10 veces.

        🔸 **Isquios (estiramiento activo tumbado):**
        - Túmbate boca arriba y eleva una pierna recta hacia el techo.
        - Sujeta el muslo o la pantorrilla (no la rodilla).
        - Flexiona y extiende ligeramente el tobillo.
        - Alterna 8–10 repeticiones por pierna.
        """,
        "imagen": None
    },
    "Movilidad torácica suave (1-2 ejercicios)": {
        "descripcion": """
        Mejora la capacidad de rotación del tronco y libera rigidez costal. Ideal tras días de golpeo intenso.

        🔸 **Apertura de libro ("lying thoracic opener"):**
        - Túmbate de lado, piernas juntas en 90º.
        - Junta ambas manos frente al pecho y abre el brazo superior hacia el lado contrario.
        - Deja que los hombros se separen y sigue la mano con la mirada.
        - Mantén 2 segundos y vuelve. Haz 10 repeticiones por lado.

        🔸 **Rotación en cuadrupedia con brazo detrás de la cabeza:**
        - Colócate en cuadrupedia.
        - Coloca una mano detrás de la cabeza.
        - Gira el tronco hacia arriba, apuntando el codo al techo.
        - Pausa arriba y vuelve. 10 repeticiones por lado.
        """,
        "imagen": None
    },
    "Estiramientos en sauna": {
        "descripcion": """
        Aprovecha el entorno cálido para ganar amplitud con menor resistencia.

        - Estira isquios, aductores, glúteos, psoas y espalda.
        - Evita posiciones forzadas o dolorosas.
        - Acompaña con respiraciones profundas.
        - Ideal como cierre de sesión de fuerza o batalla técnica.
        """,
        "imagen": None
    },
    "Correr 5 km": {
        "descripcion": "",
        "imagen": None
    },
    "Bici (rodaje tranquilo o regenerativo)": {
        "descripcion": "",
        "imagen": None
    },
    "Natación": {
        "descripcion": "",
        "imagen": None
    },
    "Desayunar": {
        "descripcion": "",
        "imagen": None
    },
    "Battlebox a las 14h (cardio, fuerza global y reacción)": {
        "descripcion": """
        Clase funcional de alta intensidad que combina movimientos atléticos, fuerza por estaciones y ejercicio al aire libre.
        - Enfócate en mantener buena postura durante desplazamientos rápidos.
        - Usa este día como entrenamiento libre y dinámico.
        """,
        "imagen": None
    }
})



for dia, ejercicios in dias.items():
    st.header(f"📆 {dia}")
    for ejercicio in ejercicios:
        with st.expander(f"▶️ {ejercicio}"):
            datos = info_ejercicios.get(ejercicio, {})
            descripcion = datos.get("descripcion", "🔸 [Ejercicio aún sin descripción]")
            imagen = datos.get("imagen")
            video = datos.get("video")
            st.markdown(descripcion)
            if imagen:
                st.image(imagen)
            if video:
                st.video(video)

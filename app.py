import streamlit as st

st.set_page_config(
    page_title="Gran Premio: Nuestro Amor - Silverstone",
    page_icon="🏎️",
    layout="centered",
)

# Estilos CSS personalizados (Temática F1 + Romance / Tonos Rojos y Rosas)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a0005 0%, #3d0a1b 50%, #1a0005 100%);
        color: #ffffff;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .card-container {
        background: rgba(255, 240, 243, 0.95);
        border: 2px solid #ff4d6d;
        border-radius: 20px;
        padding: 30px;
        color: #2b0914;
        box-shadow: 0 10px 30px rgba(255, 77, 109, 0.4);
        text-align: center;
        margin-top: 10px;
    }
    .title-f1 {
        color: #c9184a;
        font-weight: 800;
        font-size: 26px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .message-box {
        background: #fff0f3;
        border-left: 5px solid #ff4d6d;
        padding: 20px;
        border-radius: 10px;
        text-align: left;
        color: #333333;
        font-size: 16px;
        line-height: 1.6;
        margin-top: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Control de estados de la carrera
if "step" not in st.session_state:
    st.session_state.step = 1

st.markdown(
    "<h1 style='text-align: center; color: #ff758f; font-size: 24px;'>🏎️ Gran Premio Silverstone: Nuestra Historia ❤️</h1>",
    unsafe_allow_html=True,
)

# --- PASO 1: LÍNEA DE SALIDA ---
if st.session_state.step == 1:
    st.markdown(
        """
        <div class="card-container">
            <h2 class="title-f1">Línea de Meta - Silverstone</h2>
            <p style="font-size: 17px; margin: 15px 0;">El semáforo está a punto de apagarse. Arranca el gran premio de nuestras vidas, mi amol.</p>
            <div style="font-size: 55px; margin: 15px;">🏎️💨🚦</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏁 Empezar", use_container_width=True):
            st.session_state.step = 2
            st.rerun()

# --- PASO 2: LA CURVA Y EL BOTÓN ACELERAR ---
elif st.session_state.step == 2:
    st.markdown(
        """
        <div class="card-container">
            <h2 class="title-f1">Mitad de Pista (Curva Difícil)</h2>
            <p style="font-size: 17px; margin: 15px 0;">El carrito va en movimiento, pero hemos llegado a una curva complicada de la pista... ¡Es momento de dar lo mejor!</p>
            <div style="font-size: 55px; margin: 15px;">🏎️🛑🌀</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Acelerar", use_container_width=True):
            st.session_state.step = 3
            st.rerun()

# --- PASO 3: LLEGADA A LA META ---
elif st.session_state.step == 3:
    st.markdown(
        """
        <div class="card-container">
            <h2 class="title-f1">¡Línea de Meta Cruzada!</h2>
            <p style="font-size: 17px; margin: 15px 0;">¡Lo logramos mi amor! El monoplaza ha cruzado la bandera a cuadros con éxito total.</p>
            <div style="font-size: 55px; margin: 15px;">🏁🏆✨</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎁 Presiona para ver el premio", use_container_width=True):
            st.session_state.step = 4
            st.rerun()

# --- PASO 4: EL TROFEO (PISTÓN DORADO) ---
elif st.session_state.step >= 4:
    st.markdown(
        """
        <div class="card-container">
            <h2 class="title-f1">🏆 Podio de Campeones 🏆</h2>
            <!-- Trofeo de Pistón Dorado -->
            <div style="background: linear-gradient(135deg, #ffd700, #ffb703); width: 130px; height: 170px; margin: 15px auto; border-radius: 15px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 8px 25px rgba(255, 183, 3, 0.6); border: 3px solid #fff;">
                <div style="font-size: 45px;">⚙️🏆</div>
                <div style="background: #b5830d; color: white; padding: 6px 10px; font-size: 10px; font-weight: bold; border-radius: 5px; margin-top: 10px; width: 85%; text-align: center; text-transform: uppercase;">
                    la mejor novia del mundo
                </div>
            </div>
            <p style="font-size: 15px; font-weight: bold; color: #c9184a; margin-top: 10px;">¡Has ganado el gran premio de mi corazón!</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if st.session_state.step == 4:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(
                "💌 Presiona para ver el mensaje", use_container_width=True
            ):
                st.session_state.step = 5
                st.rerun()

    # --- PASO 5: EL MENSAJE DE AMOR ---
    if st.session_state.step >= 5:
        st.markdown(
            """
            <div class="message-box">
                <h3 style="color: #c9184a; margin-top: 0;">Para mi amolcitoo ❤️</h3>
                <p>Holaaaa mi amor, pues supongo que no te esperabas esto mi niña, pero te mereces mucho y espero esto te guste mi amol.</p>
                <p>El significado de esta pista es lo que vamos a construir juntos amolcitoo, habrá curvas difíciles pero crearemos estrategias buenas como las de Red Bull Racing y/o Mercedes amolcitoo, y cuando llegemos a la meta aparte de tener una pole position ganaremos el gran premio de: Nuestros esfuerzos amolcitoo y por nuestras buenas estrategias amolcitoo la meta significa el casamiento de nosotros doosh amolcitoo.</p>
                <p>Cuando sintamos que no podemos amol mío.... demos esa aceleración y eso significa que nos apoyaremos mutuamente amolcitoo, chi tu te caes yo te levantaré amol mioo, somos un equipo y aunque nuestra escudería esté conformada por nosotros tres : Dios, tu y yo.... sé que rápido daremos solución a cada problema amol mio.</p>
                <p>Contigo quiero llegar al final amolcitoo mio, contigo lo quiero todoooo no quiero a nadie mas que solamente TU. Te amo como no tienes idea amolcito mioo eres mi todoo amolcitoo gracias por darme tanto amor mi amor ❤️</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
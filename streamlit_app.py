import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Plug Remote Management", layout="wide")

    # Título y logo
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.image("https://placekitten.com/100/100", width=50)  # Placeholder para el logo
    with col2:
        st.title("Plug Remote Management")
    with col3:
        st.image("https://placekitten.com/100/100", width=50)  # Placeholder para la imagen de perfil

    # Menú lateral
    st.sidebar.title("Menu")
    st.sidebar.button("Home")
    st.sidebar.button("Control de dispositivos")
    st.sidebar.button("Gestión de programación")

    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Dispositivos", "32")
    col2.metric("Dispositivos conectados", "30")
    col3.metric("Dispositivos desconectados", "2")
    col4.metric("Programaciones Activas", "32")

    # Tabla de dispositivos
    st.subheader("Estado Dispositivos")
    data = [
        {"Usuario": "Julia Monche Riancho", "Plug ID": "000001", "Dispositivo": "Tapo P100", "Modelo": "1.0.16 Build 240529 Rel.150326", "Estado": "Conectado", "On/Off": True},
        {"Usuario": "Manuela Nieto Nuñez", "Plug ID": "000002", "Dispositivo": "Tapo P100", "Modelo": "1.0.16 Build 240529 Rel.150326", "Estado": "Desconectado", "On/Off": False},
    ]
    st.table(data)

    # Información adicional
    st.subheader("Información adicional")
    st.write("""
    Si el LED está apagado:
    - Desenchufar el dispositivo inteligente y volver a enchufarlo en la toma de corriente.
    - Probar otra toma de corriente.

    Si el LED está en naranja fijo:
    - Asegurar la estabilidad de la red Wi-Fi.
    - Mover el dispositivo inteligente más cerca del enrutador para obtener una señal más fuerte.
    - Desenchufar el dispositivo inteligente y volver a enchufarlo en la toma de corriente.
    - Si cambió el nombre de la red Wi-Fi (SSID) o la contraseña de su hogar, por favor volver a conectar el dispositivo inteligente al Wi-Fi.
    """)

if __name__ == "__main__":
    main() # main
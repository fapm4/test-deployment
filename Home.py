import streamlit as st
from utils.image import read_image
from src.styles.index import render_css

TITLE = "FindTech"
st.set_page_config(
	page_title=TITLE,
	page_icon="🔍",
	layout="wide",
	initial_sidebar_state="expanded",
)

def app():
	render_css()

	# --- HEADER ---
	img_path = 'src/assets/image.png'
	img_b64 = read_image(img_path)

	with st.container():
		st.markdown(f"""
		<div class='Header'>
			<img class='Header-logo' src='{img_b64}' alt='BuscaTech logo'/>
			<div class='Header-info'>
				<h1 class='Header-title'>{TITLE}</h1>
				<p class='Header-subtitle'>Compara productos tecnológicos y encuentra las mejores ofertas en un solo lugar.</p>
			</div>
		</div>
		""", unsafe_allow_html=True)

	# --- DESCRIPTION ---
	with st.container():
		st.markdown("""
			<div class="Description">
				<h3>Sobre el proyecto</h3>
				<p><strong>BuscaTech</strong> es una plataforma en desarrollo que busca transformar la forma en la que las personas comparan productos tecnológicos.</p>
				<p>Su objetivo es ofrecer un comparador inteligente, claro y personalizado, que permita encontrar el dispositivo más adecuado según las necesidades reales del usuario.</p>
				<p>A diferencia de los comparadores tradicionales, BuscaTech no se limita a mostrar precios o especificaciones técnicas, sino que interpreta las preferencias del usuario para ofrecer recomendaciones útiles y comprensibles.</p>
				<p>La plataforma combina información técnica, valoraciones de usuarios y comparativas entre marcas para facilitar la toma de decisiones.</p>
				<p>En esta primera fase, el proyecto se centrará en <strong>smartphones</strong> y <strong>auriculares</strong>, con un sistema de búsqueda guiada que filtra los productos según características clave como rango de precios o tamaño de pantalla.</p>
				<p>El objetivo principal es <strong>validar el interés del público</strong> y recopilar feedback para la siguiente etapa de desarrollo.</p>
				<p>BuscaTech pretende evolucionar hacia un modelo mixto de monetización basado en enlaces de afiliado y, a largo plazo, ofrecer funciones premium y una API para integrarse en otras plataformas tecnológicas.</p>
			</div>
		""", unsafe_allow_html=True)

	# --- CALL TO ACTION ---
	with st.container():
		st.markdown("""
		<div class='CTA'>
			<a href='https://forms.gle/YourFormLink' target='_blank' class='CTA-button'>
				Quiero ser tester
			</a>
		</div>
		""", unsafe_allow_html=True)

	# --- FOOTER ---
	with st.container():
		st.markdown("""
		<div class='Footer'>
			<p>© 2025 BuscaTech · Proyecto en fase inicial · Desarrollado en Streamlit</p>
			<p><a href='mailto:contacto@buscatech.com'>contacto@buscatech.com</a></p>
		</div>
		""", unsafe_allow_html=True)

if __name__ == "__main__":
	app()

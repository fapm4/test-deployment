import streamlit as st
from utils.image import read_image
from src.styles.index import render_css

TITLE = "Pickly"
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

	st.markdown(f"""
	<header class='Header'>
		<img class='Header-logo' src='{img_b64}' alt='{TITLE} logo'/>
		<div class='Header-info'>
			<h4 class='Header-subtitle'><em>Compara productos tecnológicos y encuentra las mejores ofertas en un solo lugar</em></h4>
		</div>
	</header>
	""", unsafe_allow_html=True)

	# --- DESCRIPTION ---
	
	st.markdown(f"""
	<section class="Description">
		<div class="Description-grid">
			<article class="Card">
				<h2>¿Qué es {TITLE}?</h2>
				<ul class="BulletList">
					<li><strong>{TITLE}</strong> es una nueva plataforma diseñada para ayudarte a comparar productos tecnológicos de forma más inteligente y humana.</li>
					<li>No queremos ser otro comparador de precios: queremos entender tus <strong>necesidades reales</strong> y ofrecerte recomendaciones personalizadas que te hagan sentir seguro al elegir.</li>
					<li>El objetivo es ofrecer una <strong>experiencia simple, útil y visual</strong> para todos los usuarios, sin necesidad de entender especificaciones técnicas complicadas.</li>
				</ul>
			</article>
			<article class="Card">
				<h2>En qué estamos trabajando</h2>
				<ul class="BulletList">
					<li>Estamos desarrollando un sistema de búsqueda guiada que combina <strong>inteligencia artificial y análisis de datos</strong> para ayudarte a encontrar lo que realmente te conviene.</li>
					<li>Integramos información técnica, valoraciones de usuarios y comparativas entre marcas para ofrecer una visión clara y objetiva.</li>
					<li>Queremos que puedas descubrir productos <strong>según tus prioridades</strong>: comodidad, autonomía, rendimiento o relación calidad-precio.</li>
				</ul>
			</article>
			<article class="Card">
				<h2>Fase actual del proyecto</h2>
				<ul class="BulletList">
					<li>En esta primera etapa nos enfocamos en dos tipos de producto: <strong>smartphones</strong> y <strong>auriculares</strong>.</li>
					<li>Estamos validando el interés del público y recopilando feedback de nuestros primeros usuarios.</li>
				</ul>
			</article>
		</div>
	</section>
	""", unsafe_allow_html=True)

	# --- CALL TO ACTION ---
	st.markdown("""
	<section class='CTA'>
		<p>¿Quieres ser de los primeros en probar <strong>Pickly</strong> y ayudarnos a mejorar?</p>
		<button class='CTA-button' onclick="window.open('https://forms.gle/YourFormLink', '_blank')">Pruébalo ahora</button>
		<br/><br/>
	</section>
	""", unsafe_allow_html=True)

	# --- FOOTER ---
	st.markdown("""
	<footer class='Footer'>
		<p>© 2025 Pickly · Proyecto en fase inicial · Desarrollado con amor en Streamlit</p>
		<p><a href='mailto:contacto@buscatech.com'>¡Hablemos! contacto@buscatech.com</a></p>
	</footer>
	""", unsafe_allow_html=True)

if __name__ == "__main__":
	app()

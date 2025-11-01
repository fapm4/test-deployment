import streamlit as st

def render_css():
	st.markdown("""
	<style>
		/* --- GENERAL --- */
		body {
			font-family: 'Inter', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
			color: #0f1724;
			background-color: #f5f8fb;
		}

		/* --- HEADER --- */
		header.Header {
		    display: flex;
		    flex-direction: column;
		    align-items: flex-start;
		    gap: 12px;
		    margin-bottom: 40px;
			justify-content: start;
		}
			 
		.Header-logo {
			width: 100px;
			height: auto;
			border-radius: 14px;
			box-shadow: 0 8px 20px rgba(14,165,164,0.08);
			border: 1px solid rgba(14,165,164,0.06);
			background: white;
		}

		.Header-info {
			display: flex;
			flex-direction: column;
			justify-content: center;
		}

		h1.Header-title {
			margin: 0;
			font-size: 2.4rem;
			font-weight: 800;
			color: #0ea5a4;
			letter-spacing: -0.5px;
		}

		h4.Header-subtitle {
			margin: 0;
			font-size: 1.05rem;
			color: #475569;
			margin-top: 6px;
			font-weight: 400;
		}

		/* --- DESCRIPTION --- */
		section.Description {
			max-width: 1400px;
			margin: 0 auto 60px auto;
			background: transparent;
			border-radius: 0;
			padding: 0 2rem;
		}

		section.Description h3 {
			margin-top: 0;
			color: #0b7285;
			font-weight: 700;
			font-size: 1.9rem;
			margin-bottom: 2rem;
			text-align: center;
		}

		/* --- GRID --- */
		.Description-grid {
			display: grid;
			grid-template-columns: 1fr;
			gap: 2.5rem;
		}

		/* --- CARD --- */
		article.Card {
			background: #ffffff;
			border-radius: 16px;
			padding: 2rem;
			box-shadow: 0 6px 20px rgba(2,6,23,0.06);
			border: 1px solid rgba(2,6,23,0.05);
			transition: all 0.25s ease;
			width: 100%;
			position: relative;
		}

		article.Card:hover {
			box-shadow: 0 16px 32px rgba(2,6,23,0.08);
		}

		article.Card h2 {
			margin-top: 0;
			font-weight: 700;
			margin-bottom: 1.2rem;
			font-size: 1.5rem;
			color: #0b7285;
			opacity: 0.95;
		}

		article.Card li {
			color: #334155; /* gris claro */
			font-size: 1rem;
			line-height: 1.6;
			margin-bottom: 1rem;
		}

		article.Card strong {
			font-weight: 600;
			color: black;
		}

		/* --- BULLET LIST --- */
		.BulletList {
			list-style: none;
			margin: 0;
			padding: 0;
		}

		.BulletList li {
			position: relative;
			margin-bottom: 0.9rem;
			padding-left: 1.4rem;
		}

		.BulletList li::before {
			content: "›";
			position: absolute;
			left: 0;
			top: 0;
			color: #0ea5a4;
			font-weight: 900;
			font-size: 1rem;
			line-height: 1.6;
			opacity: 0.8;
		}

		/* --- CTA --- */
		section.CTA {
			text-align: center;
			margin: 60px 0;
		}

		section.CTA h2 {
			font-size: 1.8rem;
			color: #0f172a;
			margin-bottom: 1rem;
		}

		section.CTA p {
			font-size: 1rem;
			color: #475569;
			margin-bottom: 1.5rem;
		}

		.CTA-button {
			display: inline-block;
			background: linear-gradient(90deg, #0f172a 0%, #334155 100%);
			color: white !important;
			padding: 14px 40px;
			border-radius: 12px;
			font-size: 1.05rem;
			font-weight: 700;
			text-decoration: none !important;
			transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease;
			box-shadow: 0 10px 30px rgba(15,23,42,0.18);
			border: none;
		}

		.CTA-button:hover {
			transform: translateY(-3px);
			filter: brightness(0.97);
			box-shadow: 0 16px 36px rgba(15,23,42,0.25);
		}

		/* --- FOOTER --- */
		footer.Footer {
			text-align: center;
			color: #6b7280;
			font-size: 0.9rem;
			margin-top: 80px;
			padding: 30px 10px;
			border-top: 1px solid rgba(2,6,23,0.04);
		}

		footer.Footer a {
			color: #0ea5a4;
			text-decoration: none;
			font-weight: 600;
		}

		footer.Footer a:hover {
			text-decoration: underline;
		}
	</style>
	""", unsafe_allow_html=True)

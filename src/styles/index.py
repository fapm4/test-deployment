import streamlit as st

def render_css():
    st.markdown("""
    <style>
        /* --- GENERAL --- */
        body {
            font-family: 'Inter', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
            color: #0f1724;
            background-color: #f5f8fb; /* suave y claro */
        }

        /* --- HEADER --- */
        .Header {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 40px;
        }

        .Header-logo {
            width: 100px;
            height: auto;
            border-radius: 14px;
            box-shadow: 0 8px 20px rgba(14,165,164,0.08); /* acento suave */
            border: 1px solid rgba(14,165,164,0.06);
            background: white;
        }

        .Header-info {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .Header-title {
            margin: 0;
            font-size: 2.4rem;
            font-weight: 800;
            color: #0ea5a4; /* acento teal */
            letter-spacing: -0.5px;
        }

        .Header-subtitle {
            margin: 0;
            font-size: 1.05rem;
            color: #475569; /* gris azulado para buena legibilidad */
            margin-top: 6px;
        }

        /* --- DESCRIPTION --- */
        .Description {
            max-width: 1500px;
            margin: 0 auto 50px auto;
            background: linear-gradient(180deg, #ffffff 0%, #f7fbfc 100%);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(2,6,23,0.06);
            border: 1px solid rgba(2,6,23,0.04);
            line-height: 1.7;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }

        .Description:hover {
            transform: translateY(-4px);
            box-shadow: 0 18px 40px rgba(2,6,23,0.08);
        }

        .Description h3 {
            margin-top: 0;
            color: #0b7285; /* tono más oscuro del acento */
            font-weight: 700;
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }

        .Description p {
            margin-bottom: 1rem;
            color: #274157; /* texto principal un poco suave */
        }

        /* --- CTA BUTTON --- */
        .CTA {
            text-align: center;
            margin: 50px 0;
        }

        .CTA-button {
            display: inline-block;
            background: linear-gradient(90deg, #06b6d4 0%, #0ea5a4 100%);
            color: white !important;
            padding: 14px 40px;
            border-radius: 12px;
            font-size: 1.05rem;
            font-weight: 700;
            text-decoration: none !important;
            transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease;
            box-shadow: 0 10px 30px rgba(14,165,164,0.16);
            border: none;
        }

        .CTA-button:hover {
            transform: translateY(-3px);
            filter: brightness(0.98);
            box-shadow: 0 16px 36px rgba(14,165,164,0.2);
        }

        /* --- FOOTER --- */
        .Footer {
            text-align: center;
            color: #6b7280;
            font-size: 0.9rem;
            margin-top: 80px;
            padding: 30px 10px;
            border-top: 1px solid rgba(2,6,23,0.04);
        }

        .Footer a {
            color: #0ea5a4;
            text-decoration: none;
            font-weight: 600;
        }

        .Footer a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)
import streamlit as st
from scrape import scrape_website
from pathlib import Path

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the Website...")
    result = scrape_website(url)

    if result:
        # Caminho do arquivo .txt na mesma pasta do projeto
        output_path = Path(__file__).parent / "scraped_result.txt"

        # Salva o resultado no arquivo
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)

        st.success(f"✅ Resultado salvo em: {output_path}")
    else:
        st.error("⚠️ Nenhum conteúdo obtido.")

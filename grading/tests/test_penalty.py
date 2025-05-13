from bs4 import BeautifulSoup
# Helper function to load the HTML content
def parse_html():
    with open("index.html", "r") as file:
        return BeautifulSoup(file, "html.parser")

def test_no_bootstrap_used():
    """
    pass: Classes do Bootstrap foram encontradas no HTML.
    fail: Nenhuma classe do Bootstrap foi detectada. É obrigatório utilizar Bootstrap na construção da página.
    """
    soup = parse_html()
    classes = [cls for tag in soup.find_all(class_=True) for cls in tag.get('class', [])]
    bootstrap_classes = [cls for cls in classes if cls.startswith(('container', 'row', 'col', 'btn', 'navbar'))]
    assert not bootstrap_classes, "Você utilizou corretamente as classes Bootstrap"

def test_no_sections():
    """
    pass: Seções principais estão devidamente presentes no HTML.
    fail: As seções obrigatórias estão ausentes. Adicione seções com os IDs: apresentacao, habilidades, aprendizado, contato.
    """
    soup = parse_html()
    section_ids = ['apresentacao', 'habilidades', 'aprendizado', 'contato']
    missing = [sid for sid in section_ids if soup.find(id=sid) is None]
    assert missing, f"Seções presentes!"

def test_no_contact_info():
    """
    pass: Informações de contato (e-mail, redes sociais ou link) foram encontradas.
    fail: Nenhuma informação de contato foi detectada. Adicione dados de contato na seção apropriada.
    """
    soup = parse_html()
    contact_keywords = ['mailto:', 'linkedin.com', 'github.com', 'instagram.com', 'facebook.com']
    links = soup.find_all('a', href=True)
    found = any(any(keyword in link['href'] for keyword in contact_keywords) for link in links)
    assert not found, ("Informações de contato válidas encontradas.")

def test_incorrect_html_structure():
    """
    pass: O HTML está bem estruturado e contém as principais tags básicas.
    fail: A estrutura do HTML está incorreta. Certifique-se de incluir <!DOCTYPE>, <html>, <head> e <body>.
    """
    soup = parse_html()
    html = soup.find('html')
    head = soup.find('head')
    body = soup.find('body')
    assert html is None and head is None and body is None, "Estrutura básica do HTML está completa."

def test_uses_inline_styles_only():
    """
    pass: A página utiliza estilos externos ou internos adequadamente.
    fail: Apenas estilos inline foram encontrados. Use <style> no <head> ou um arquivo CSS externo.
    """
    soup = parse_html()
    has_external_or_internal_style = bool(soup.find('link', rel='stylesheet') or soup.find('style'))
    assert not has_external_or_internal_style, "Estilos inline não foram identificados."

def test_uses_table_for_layout():
    """
    pass: Tabelas são usadas apenas para dados tabulares.
    fail: Tabela foi usada para layout. Evite utilizar <table> para estrutura visual da página.
    """
    soup = parse_html()
    tables = soup.find_all('table')
    suspicious = [table for table in tables if len(table.find_all(['th', 'td'])) < 2]
    assert suspicious, "Tabelas de uso indevido para layout não encontradas."

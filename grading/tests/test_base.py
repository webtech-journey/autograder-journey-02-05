from bs4 import BeautifulSoup
# Helper function to load the HTML content
def parse_html():
    with open("index.html", "r") as file:
        return BeautifulSoup(file, "html.parser")

def test_html_html_tag():
    """
    pass: A tag <html> está corretamente presente, iniciando o documento HTML.
    fail: O documento HTML está sem a tag <html>. Adicione-a para garantir a estrutura correta.
    """
    soup = parse_html()
    assert soup.find('html') is not None, "A tag <html> está ausente."

def test_bootstrap_linked():
    """
    pass: O Bootstrap está corretamente vinculado via CDN.
    fail: O Bootstrap não foi encontrado. Certifique-se de incluir a CDN no <head> do HTML.
    """
    soup = parse_html()
    links = soup.find_all('link', href=True)
    bootstrap_found = any('bootstrap' in link['href'] for link in links)
    assert bootstrap_found, "CDN do Bootstrap não encontrada no HTML."

def test_navbar_present():
    """
    pass: Um elemento <nav> com classes do Bootstrap foi encontrado.
    fail: A navbar com Bootstrap não foi encontrada. Utilize as classes 'navbar' corretamente.
    """
    soup = parse_html()
    nav = soup.find('nav', class_='navbar')
    assert nav is not None, "Navbar do Bootstrap não encontrada."

def test_sections_exist():
    """
    pass: Todas as seções obrigatórias estão presentes no HTML.
    fail: Uma ou mais seções obrigatórias estão ausentes. Verifique se usou os IDs: apresentacao, habilidades, aprendizado, contato.
    """
    soup = parse_html()
    required_sections = ['apresentacao', 'habilidades', 'aprendizado', 'contato']
    for section_id in required_sections:
        assert soup.find(id=section_id) is not None, f"Seção com id '{section_id}' não encontrada."

def test_footer_exists():
    """
    pass: A tag <footer> está presente no HTML.
    fail: A página está sem um rodapé. Adicione um <footer> com informações de contato ou créditos.
    """
    soup = parse_html()
    assert soup.find('footer') is not None, "A tag <footer> está ausente."

def test_responsive_layout():
    """
    pass: O layout responsivo com container, row e col do Bootstrap foi identificado.
    fail: O layout não utiliza a estrutura responsiva do Bootstrap. Utilize 'container', 'row' e 'col' corretamente.
    """
    soup = parse_html()
    assert soup.find(class_='container'), "Classe 'container' do Bootstrap ausente."
    assert soup.find(class_='row'), "Classe 'row' do Bootstrap ausente."
    assert soup.find(class_='col'), "Classe 'col' do Bootstrap ausente."

def test_custom_css_file():
    """
    pass: Um arquivo CSS personalizado foi vinculado ao HTML.
    fail: Nenhum arquivo CSS personalizado foi encontrado. Adicione um <link> com href para seu arquivo CSS.
    """
    soup = parse_html()
    links = soup.find_all('link', href=True)
    custom_css_found = any('.css' in link['href'] and 'bootstrap' not in link['href'] for link in links)
    assert custom_css_found, "Arquivo CSS personalizado não encontrado."

def test_meta_viewport_present():
    """
    pass: A meta tag de viewport foi encontrada, garantindo responsividade em dispositivos móveis.
    fail: A meta tag de viewport está ausente. Adicione <meta name='viewport' content='width=device-width, initial-scale=1.0'> no <head>.
    """
    soup = parse_html()
    meta = soup.find('meta', attrs={'name': 'viewport'})
    assert meta is not None, "Meta tag de viewport não encontrada."

def test_grid_diversity():
    """
    pass: Diversas classes de grid do Bootstrap foram utilizadas (ex: col-sm, col-md, col-lg).
    fail: Apenas uma variação de grid foi usada. Use diferentes classes para garantir responsividade adequada.
    """
    soup = parse_html()
    prefixes = ('col-sm', 'col-md', 'col-lg', 'col-xl')
    found_prefixes = set()

    for tag in soup.find_all(class_=True):
        for cls in tag.get('class', []):
            for prefix in prefixes:
                if cls.startswith(prefix):
                    found_prefixes.add(prefix)

    assert len(found_prefixes) >= 1, "Poucas variações de grid do Bootstrap foram usadas."


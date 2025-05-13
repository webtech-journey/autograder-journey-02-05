from bs4 import BeautifulSoup
# Helper function to load the HTML content
def parse_html():
    with open("index.html", "r") as file:
        return BeautifulSoup(file, "html.parser")


def test_fontawesome_used():
    """
    pass: O FontAwesome foi corretamente vinculado e está sendo usado para ícones.
    fail: FontAwesome não foi encontrado. Considere adicionar ícones para enriquecer visualmente a página.
    """
    soup = parse_html()
    links = soup.find_all('link', href=True)
    fa_linked = any('fontawesome' in link['href'].lower() for link in links)
    fa_used = bool(soup.find('i', class_=lambda x: x and 'fa' in x))
    assert fa_linked and fa_used, "FontAwesome não está sendo utilizado."

def test_profile_picture_used():
    """
    pass: Uma imagem de perfil está presente na apresentação.
    fail: Nenhuma imagem de perfil foi encontrada. Adicione uma imagem para tornar a apresentação mais pessoal.
    """
    soup = parse_html()
    img = soup.find('img')
    assert img is not None and img.get('alt'), "Imagem de perfil ausente ou sem atributo alt."

def test_contact_button_functional():
    """
    pass: Um botão estilizado foi encontrado com funcionalidade de contato (e-mail ou link).
    fail: Botão de contato ausente ou sem ação. Adicione um botão com 'mailto:' ou link funcional.
    """
    soup = parse_html()
    button = soup.find('a', class_=lambda x: x and 'btn' in x)
    assert button is not None and (button.get('href', '')), "Botão de contato não funcional."

def test_custom_classes_used():
    """
    pass: Classes personalizadas estão sendo usadas além das do Bootstrap.
    fail: Nenhuma classe personalizada encontrada. Personalize seu site além dos estilos prontos do Bootstrap.
    """
    soup = parse_html()
    elements = soup.find_all(class_=True)
    custom_classes = [el['class'] for el in elements if any('container' not in c and 'row' not in c and 'col' not in c and 'btn' not in c and 'navbar' not in c for c in el['class'])]
    assert custom_classes, "Nenhuma classe personalizada identificada."

def test_hover_effects_or_transitions():
    """
    pass: Efeitos visuais como hover ou transições foram identificados no CSS externo.
    fail: Nenhum efeito visual detectado no CSS externo. Adicione efeitos no arquivo style.css, evitando estilos inline.
    """
    try:
        with open("styles.css", "r", encoding="utf-8") as f:
            css = f.read()
    except FileNotFoundError:
        assert False, "Arquivo style.css não encontrado."

    has_hover = ":hover" in css or "transition" in css
    assert has_hover, "Efeito de hover ou transição não identificado no CSS externo."

def test_accessibility_attributes():
    """
    pass: Atributos de acessibilidade como alt, aria ou label foram utilizados.
    fail: Nenhum atributo de acessibilidade identificado. Considere adicionar 'alt', 'aria-*' ou 'label'.
    """
    soup = parse_html()
    has_alt = bool(soup.find('img', alt=True))
    has_aria = bool(soup.find(attrs={k: True for k in ['aria-label', 'aria-hidden', 'aria-labelledby']}))
    has_label = bool(soup.find('label'))
    assert has_alt or has_aria or has_label, "Atributos de acessibilidade não encontrados."

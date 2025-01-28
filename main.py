from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO

# Inicializando o navegador com Selenium (sem interface gráfica)
options = Options()
options.add_argument('--headless')  # Faz o navegador funcionar sem abrir a janela
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Desabilitar SSL
# options.add_argument('--ignore-certificate-errors')

# Inicializa o driver do Chrome com o Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Acesse o site desejado
driver.get("https://zclt.github.io/projects/to-na-vaca/")

# Capture a tela (screenshot) da página
screenshot = driver.get_screenshot_as_png()

# Converta a captura de tela para um objeto de imagem usando Pillow
image = Image.open(BytesIO(screenshot))

# Salve a imagem
image.save("screenshot.png")

# Feche o driver
driver.quit()

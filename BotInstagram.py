from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import GravarLog as log

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\User\Projetos\bot_instagram\geckodriver.exe"
        )
        # LINK DE DOWNLOAD DO GECKODRIVER: https://github.com/mozilla/geckodriver/releases
        # LINK DE DOWNLOAD DO FIREFOX: https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(10)
        # login_button = driver.find_element_by_xpath(
        #     "//a[@href='/accounts/login/?source=auth_switcher']"
        # )
        # login_button.click()
        # time.sleep(3)

        # SELECIONA O CAMPO LOGIN E INSERE DADOS
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        # SELECIONA O CAMPO SENHA E INSERE DADOS
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        # BOTAO ENTER
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        # URL DA FOTO
        url = "https://www.instagram.com/p/CR9KFU2M-gF/"
        self.comentarios(
            url
        )

    # MÉTODO PARA SIMULAR A DIGITAÇÃO HUMANA
    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(2, 5) / 30)

    def comentarios(self, url):
        # PERSONALIZAR COMENTARIOS
        comentarios = ["Deus abençoa!", "Boa Sorte à todos!", "#EuQuero", "Quero o PIX!!", "Desejo sorte a todos os participantes!",
                       "Esse prêmio será meu!!", "Jesus conduz e determina, s244", "Sigam o perfil @nserv.informatica", "Sigam meu perfil oficial @ncesar.97", "@jemacmoveis", 
                       "@cissarabelomakeup", "@ncesar.sorteios", "@ncsar.acessoria", "@ncesar.premios", "Que Deus ilumine o caminho de todos", 
                       "@lio44_", "Deus é fiel!"]
        indice = 0
        error = 0
        # PARÂMETRO NÚMERO DE REPETIÇÃO
        repeticao = 1000

        # ACESSA URL DA FOTO INFORMADA
        driver = self.driver
        driver.get(url)
        time.sleep(5)

        while indice < repeticao:
            try:
                # SELECIONA O CAMPO COMENTÁRIOS
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(5, 10))

                # INSERE UM COMENTÁRIO DE FORMA ALEATÓRIA
                self.type_like_a_person(random.choice(
                    comentarios), comment_input_box)
                time.sleep(random.randint(5, 10))

                # CLICA EM PUBLICAR
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                indice = indice + 1
                print(indice)
                time.sleep(random.randint(120, 240))
            except Exception as e:  
                log.GravarLog(indice)
                error = error + 1
                print(e)
                print(error)
                time.sleep(random.randint(1800, 3600))
                self.comentarios(
                    url
                )

# USUARIO E SENHA DO INSTAGRAM
mrRobbot = InstagramBot("usuario", "login")
mrRobbot.login()

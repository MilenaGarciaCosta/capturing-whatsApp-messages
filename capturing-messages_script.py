from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Configuração do navegador Edge
edge_options = Options()
edge_options.add_argument("--log-level=3")
edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])

caminho_edgedriver = r"C:\WebDriver\msedgedriver.exe" # Esse driver deve estar em algum local da máquina, esse caminho deve levar a ele
service = Service(caminho_edgedriver)
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window() # Deixando a tela do nagevador maximizada

try:
    # Abre o WhatsApp Web
    driver.get("https://web.whatsapp.com")

    # Aguarda o login manual
    input("Escaneie o QR code, espere os chats carregarem e então pressione Enter para continuar...")

    # Aguarda o carregamento do chat
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        )
        print("Chat carregado com sucesso!\n")
    except Exception as e:
        print(f"Erro ao carregar o chat: {str(e)}")
        driver.quit()
        exit()

    # Variável para armazenar a última mensagem capturada
    ultima_mensagem = """"""

    # Função para capturar a última mensagem
    def capturar_ultima_mensagem():
        mensagens = driver.find_elements(By.CSS_SELECTOR, "div[class*='message-in']")
        if mensagens:
            return mensagens[-1].text
        return None
    
    # Função para tratar mensagem capturada
    def tratar_mensagem(mensagem):
        mensagem = mensagem.lower()

        # Definir padrões para capturar somente as informações relevates (aceitando espaços OU quebras de linha)
        padrao = r"nome:(?P<nome>.+?)\s*(?:local:|$)(?P<local>.+?)\s*(?:problema:|$)(?P<problema>.+?)(?P<horario>\d{1,2}:\d{2})\s*$" # Horário é uma informação que vem automáticamente com a mensagem capturada

        # Procurar padrão na mensagem
        match = re.search(padrao, mensagem, re.DOTALL) # re.DOTALL captura também quebras de linha (para caso o usuário envie e mensagem com quebra de conteúdo utilizando Enter)

        # Se o padrão for encontrado, agrupar os valores removendo espaços, virgulas indesejadas no nome e local e capitalizando para manter consistência
        if match:
            nome = match.group("nome").strip().replace(",", "").capitalize()
            local = match.group("local").strip().replace(",", "").capitalize()
            problema = match.group("problema").strip().capitalize()
            horario = match.group("horario").strip()

            # Imprime aos valores agrupados de maneira padronizada
            print(f"Nome: {nome}\nLocal: {local}\nProblema: {problema}\nHorário: {horario}\n")
        else:
            print("Erro: Mensagem formatada incorretamente.\n")

    # Loop para monitorar novas mensagens
    try:
        while True:
            nova_mensagem = capturar_ultima_mensagem()

            if nova_mensagem and nova_mensagem != ultima_mensagem:
                ultima_mensagem = nova_mensagem
                # Imprime mensagem original sem tratamento
                print(f"Nova mensagem: {ultima_mensagem}\n")

                tratar_mensagem(nova_mensagem)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoramento interrompido.")

except Exception as e:
    print(f"Erro durante a execução: {str(e)}")
finally:
    driver.quit()
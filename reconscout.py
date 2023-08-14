import subprocess


# BANNER

def generar_banner(texto):
    colores = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    reset_color = "\033[0m"

    banner = ""
    color_index = 0

    for letra in texto:
        banner += colores[color_index] + letra
        color_index = (color_index + 1) % len(colores)

    banner += reset_color

    return banner


texto_banner = f"""

,---.                    ,---.               |    
|---',---.,---.,---.,---.`---.,---.,---..   .|--- 
|  \ |---'|    |   ||   |    ||    |   ||   ||    
`   ``---'`---'`---'`   '`---'`---'`---'`---'`---'
by theRonin

"""
banner = generar_banner(texto_banner)
print(banner)

# VERIFICACIÓN DE PAQUETES

print("[+]Verificando existencia de paquetes necesarios en el sistema")


def verificar_paquete(paquete):
    try:
        subprocess.check_output(["dpkg", "-s", paquete], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def instalar_paquete(paquete):
    try:
        subprocess.check_call(["sudo", "apt", "install", "-y", paquete])
        print(f"✓ {paquete} instalado")
    except subprocess.CalledProcessError:
        print(f"✗ No se pudo instalar {paquete}")


def imprimir_mensaje(texto, color):
    colores = {
        "verde": "\033[32m",
        "rojo": "\033[31m",
        "reset": "\033[0m"
    }
    print(f"{colores[color]}{texto}{colores['reset']}")


# Lista de paquetes a verificar
paquetes_a_verificar = ["curl", "nmap", "wireshark", "metasploit-framework", "whois", "theHarvester", "nikto",
                        "dnsrecon", "dnsmap", "dnsenum", "subfinder", "wpscan", "fierce", "maltego", "sublist3r",
                        "urlextractor", "dmitry", "amap"]

# Verificar si los paquetes están instalados y imprimir mensajes
for paquete in paquetes_a_verificar:
    if verificar_paquete(paquete):
        imprimir_mensaje(f"✓ {paquete} encontrado", "verde")
    else:
        imprimir_mensaje(f"✗ {paquete} no está instalado", "rojo")
        respuesta = input(f"Desea instalar {paquete}? (y/n): ").strip().lower()
        if respuesta == "y":
            instalar_paquete(paquete)
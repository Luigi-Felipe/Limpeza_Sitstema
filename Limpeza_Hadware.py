import os
import subprocess
import ctypes
import sys

def is_admin():
    """Verifica se o script está sendo executado como administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_commands():
    if not is_admin():
                                                   # Re-executa o script com privilégios de administrador
        print("Solicitando privilégios de administrador...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    print("--- Iniciando Limpeza e Diagnóstico ---")

                                     #Abrir pastas temporárias (Simulando o Windows + R)
    
    temp_paths = [os.environ.get('TEMP'), r'C:\Windows\Temp']
    
    for path in temp_paths:
        print(f"Abrindo pasta temporária: {path}")
        try:
            # Abre a pasta no Explorador de Arquivos
            os.startfile(path)
        except Exception as e:
            print(f"Erro ao abrir {path}: {e}")

    # 2. Executar SFC /SCANNOW no CMD
    print("\nIniciando Verificador de Arquivos do Sistema (SFC /SCANNOW)...")
    print("Isso pode levar alguns minutos. Não feche a janela.")
    
    try:
                                                               # Executa o comando e aguarda a finalização
        processo = subprocess.run(["sfc", "/scannow"], shell=True)
        
        if processo.returncode == 0:
            print("\nSFC concluído com sucesso!")
        else:
            print("\nSFC finalizado. Verifique os logs acima para detalhes.")
            
    except Exception as e:
        print(f"Erro ao executar SFC: {e}")

    input("\nProcesso finalizado. Pressione Enter para sair...")

if __name__ == "__main__":
    run_commands()
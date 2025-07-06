import os

# Caminho para a pasta onde os vídeos estão localizados
folder_path = "D:\\Alex\\Learning\\PHP\\Laravel"
Videos = []

# Função para iterar e renomear os arquivos de vídeo
def rename_videos(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".mp4"):  # Filtrar apenas arquivos de vídeo com extensão .mp4
            # Extrair parte do nome do arquivo, similar ao Teste.py
            parte_extraida = file_name[-15:-13]
            print(parte_extraida)
            # Concatenar a parte extraída com o nome do arquivo
            novo_nome = parte_extraida + " " + file_name
            # Caminho completo para o arquivo antigo e novo
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, novo_nome)
            # Renomear o arquivo
            os.rename(old_file_path, new_file_path)
            print(f"Renomeado: {file_name} -> {novo_nome}")

# Chama a função para renomear os vídeos
rename_videos(folder_path)

import os
import glob

# Caminho da pasta de downloads
downloads_path = 'D:\\Alex\\Learning\\React Native'  # Use \\ para evitar problemas de escape

# Caminho do arquivo da playlist M3U
playlist_file_path = os.path.join(downloads_path, 'playlist_vlc.m3u')

# Lista para armazenar os vídeos organizados
playlist = []

# Listar arquivos na pasta de downloads
for i in range(1, 47):  # De 01 a 46
    # Procurar arquivos que terminem com "(720_HD).mp4" e contenham "aula" no nome
    search_pattern = f'*Aula {str(i).zfill(2)}(720P HD).mp4'
    print(search_pattern)
    found_video = False  # Variável para verificar se o vídeo foi encontrado

    for original_file_path in glob.glob(os.path.join(downloads_path, search_pattern)):
        found_video = True  # Vídeo encontrado
        # Novo nome com prefixo numérico
        original_filename = os.path.basename(original_file_path)
        new_filename = f'{str(i).zfill(2)}...{original_filename}'
        new_file_path = os.path.join(downloads_path, new_filename)
        
        # Renomear o arquivo
        os.rename(original_file_path, new_file_path)
        

    if found_video:
        print(f'Vídeo(s) encontrado(s) para aula {str(i).zfill(2)}.')
    else:
        print(f'Nenhum vídeo encontrado para aula {str(i).zfill(2)}.')

# Criar um arquivo M3U com a playlist
with open(playlist_file_path, 'w') as f:
    f.write('#EXTM3U\n')  # Cabeçalho do arquivo M3U
    for video in playlist:
        f.write(f'#EXTINF:-1,{os.path.basename(video)}\n')  # Informações do vídeo
        f.write(video + '\n')  # Caminho do vídeo

print("Vídeos renomeados e log gerado com sucesso!")

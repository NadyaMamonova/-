import vK, yandex_disk


if __name__ == '__main__':
    user1 = vK.VK(user_id='', token='')
    user1.get_photos(user_id='')
    user1 = yandex_disk.YandexDisk(token='')
    user1.create_folder(folder='')
    user1.upload_file(folder='')
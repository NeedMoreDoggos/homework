def check_wav(string, audi_f=320, channels=2, sampling=44100, bit_depth=16):
    """
    "Работаем" с wav файлом.
    :param string: Путь к аудиофайлу: должен заканчиваться именем файла с расширением .wav.
    :param audi_f: Аудиоформат: целое число или строка в диапазоне от 0 до 9999.
    :param channels: Количество каналов: целое число или строка в диапазоне от 1 до 10.
    :param sampling: Частота дискретизации (сэмплирования): целое число или строка из списка допустимых значений (8000,
            11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000).
    :param bit_depth: Разрядность (битовая глубина): целое число или строка из списка допустимых значений (8, 16, 24, 32).
    :return: True - данные корректны. False - нет.
    """
    samp = (8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000)
    bd = (8, 16, 24, 32)
    chan = range(1, 11)
    af = range(0, 10_000)
    audi_f, channels, sampling, bit_depth = list(map(int, [audi_f, channels, sampling, bit_depth]))

    if string[len(string) - 3:] != 'wav':
        return False
    if not audi_f in af:
        return False
    if not channels in chan:
        return False
    if not sampling in samp:
        return False
    if not bit_depth in bd:
        return False
    return True

print(check_wav('sdsad.wav', bit_depth='32', sampling=8000, audi_f=1000000))
latin = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def lat_conv(lat_namber):
    if lat_namber == '':
        return 0
    if len(lat_namber) > 1:
        if latin[lat_namber[0]] < latin[lat_namber[1]]:
            return  latin[lat_namber[1]] - latin[lat_namber[0]] + lat_conv(lat_namber[2:])
    return latin[lat_namber[0]] + lat_conv(lat_namber[1:])


print(lat_conv('MXCIX'))
# 1099

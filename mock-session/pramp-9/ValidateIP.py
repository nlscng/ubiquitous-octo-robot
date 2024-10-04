def validateIP(ip):
    """
    @param ip: str
    @return: bool
    """
    if ip.count('.') != 3:
        return False

    tokens = ip.split('.')
    if len(tokens) != 4:
        return False

    for one_token in tokens:
        try:
            int_token = int(one_token)
        except:
            print("Invalid format, expecting int between 0 and 255 inclusive in a single block")
            return False

        if int_token < 0 or int_token > 255:
            return False
    return True


assert validateIP("192.168.0.1")
assert validateIP("0.0.0.0")
assert validateIP("123.24.59.99")
assert not validateIP("1.2.3.4.5")
assert not validateIP("1..23.4")
assert not validateIP("1.256.3.4")
assert not validateIP(".254.255.0")

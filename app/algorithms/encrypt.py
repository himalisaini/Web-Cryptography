from fileenc_openssl import stretch_key, encrypt_file, decrypt_file

def encrypt_fun(loc,code):

    stretched_key = stretch_key(code)

    pth = loc
    res_pth = encrypt_file(loc, key=stretched_key)
    return res_pth
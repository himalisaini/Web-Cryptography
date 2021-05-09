from fileenc_openssl import stretch_key, encrypt_file, decrypt_file

def decrypt_fun(loc,code):

    stretched_key = stretch_key(code)

    pth = loc
    res_pth = decrypt_file(loc, key=stretched_key)
    return res_pth
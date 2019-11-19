import hashlib


def md5(pwd):
    md5_obj = hashlib.md5()
    md5_obj.update(pwd.encode())
    res = md5_obj.hexdigest()
    print(res)
    # md5: e10adc3949ba59abbe56e057f20f883e  撞库

    # sha1: 210a28f50a8e9a0986df287ac9ae224de95b8978
    # sha256: 52f1476494897c64f417deb7ef7cd690f1cea9edce638746c420f1240d3d39dc
    # sha512: 816d8d4fa68c44c57b59eacc08fa8eaee4e1b550c8e0a058c13bb7117a773414cd6feaca12dabcf15f58fc9a5bd071f26b716f43d7f69df5054caabf2f58e74c
md5('123456')


def md5(pwd):
    md5_obj = hashlib.md5('123'.encode())  # 加盐，提高安全性
    md5_obj.update(pwd.encode())
    res = md5_obj.hexdigest()
    print(res)
    # md5: 1e191d851b3b49a248f4ea62f6b06410

md5('123456')


def md5(user, pwd):
    md5_obj = hashlib.md5(user.encode())  # 加盐，提高安全性
    md5_obj.update(pwd.encode())
    res = md5_obj.hexdigest()
    print(res)
    # md5: 94e4320348110efd343e70a99864a535


md5('yang', '123456')
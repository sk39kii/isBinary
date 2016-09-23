# -*- coding: utf-8 -*-

import chardet
import mimetypes
import os.path
import sys


def isBinary(target):
    u"""バイナリファイル判定
    MIMEタイプで判別、MIMEで判別不能な時は、中身のデータで判別
    """
    ret = False
    m = mimetypes.guess_type(target)[0]
    if m is None:
        # MIMEで判別不能の場合(拡張子なしなど?)
        # ret = True

        # ファイルの中身で判断(chardetのエンコードで判断)
        buf = readdump(target, 'rb')
        encode = chardet.detect(buf)['encoding']

        # エンコード不明時はバイナリとする
        if encode is None:
            ret = True

        # アスキーコードの08H以下(制御文字)の文字がある場合はバイナリ
        if isBinary08HCharacter(buf):
            ret = True

    elif m.find('office') > -1:
        ret = True
    elif m.startswith('image'):
        ret = True
    elif m.startswith('text'):
        ret = False
    elif m.startswith('application/vnd.ms-excel'):
        # これはCSV
        ret = False
    return ret


def isBinary08HCharacter(buf):
    u"""バイナリファイル判定
    ファイルの中身を開きASCIIコードの08H以下があるかどうかで判別
    """
    ret = False
    l = map(ord, list(buf))
    for n in range(0, 9):
        if n in l:
            ret = True
            break
    return ret


def readdump(dumpname, mode='r'):
    u"""ファイルの読み込み
    """
    buf = ''
    with open(dumpname, mode) as f:
        buf = f.read()
    return buf

if __name__ == "__main__":
    p = sys.argv[1]
    print u'{} is Binary? : {}'.format(p, isBinary(p))

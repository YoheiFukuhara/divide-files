# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
import shutil
import os
import subprocess

# 基本モデル
FLAGS = None

def upload_move(path, num):

    # フォルダなかったら作成(フォルダと配下にファイルがあっても消されない)
    p_done_dir = Path(FLAGS.base_dir) / path
    os.makedirs(p_done_dir, exist_ok=True)

    for i, file in enumerate(sorted(list(Path(FLAGS.base_dir).iterdir()))):

        if i == num:
            break

        li_result = [b""]

        while li_result[-1].decode('utf-8').find("100.00%") == -1:
            cmd = "cf sapml fs put " + str(file) + " " + FLAGS.upload.format(path)
            print(cmd)
            runcmd = subprocess.check_output(cmd.split())
            li_result = runcmd.splitlines()
            print(li_result[-1].decode('utf-8'))
        else:
            shutil.move(str(file), str(p_done_dir))


def main():
    # prepare_dir()
    upload_move("training", FLAGS.training)
    upload_move("validation", FLAGS.validation)
    upload_move("test", FLAGS.test)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b',
        '--base_dir',
        type=str,
        default='/home/i348221/Apps/python/fax/ocr/20.image/done/f2',
        help='base directory'
    )
    parser.add_argument(
        '-tr',
        '--training',
        type=int,
        default=800,
        help='Number of files for training'
  )
    parser.add_argument(
        '-v',
        '--validation',
        type=int,
        default=100,
        help='Number of files for validation'
    )
    parser.add_argument(
        '-te',
        '--test',
        type=int,
        default=100,
        help='Number of files for test'
    )
    parser.add_argument(
        '-u',
        '--upload',
        type=str,
        default='fax/{}/f2/',
        help='directory to upload'
    )

    FLAGS, unparsed = parser.parse_known_args()
    main()
# -*- coding: utf-8 -*-

import argparse
import pathlib
import shutil
import os

# 基本モデル
FLAGS = None
FINISH = "99.Done"


def prepare_dir():
    # フォルダなかったら作成(フォルダと配下にファイルがあっても消されない)
    p_done_dir = pathlib.Path(FLAGS.base_dir) / FINISH
    os.makedirs(p_done_dir, exist_ok=True)

    for i in range(FLAGS.directory):
        p_sub_dir = pathlib.Path(FLAGS.base_dir) / str(i)

        # フォルダがあったら中のファイルを移動
        if p_sub_dir.exists():
            for file in p_sub_dir.iterdir():
                shutil.move(str(file), str(p_done_dir))

        # フォルダなかったら作成
        else:
            os.makedirs(p_sub_dir)


def move_files():

    for i in range(FLAGS.directory):
        p_sub_dir = pathlib.Path(FLAGS.base_dir) / str(i)
        print("cf sapml fs put {}/ {}".format(str(p_sub_dir), FLAGS.upload))
        i_file = 0

        for p_obj in pathlib.Path(FLAGS.base_dir).iterdir():
            if p_obj.is_file():
                i_file += 1
                shutil.move(str(p_obj), str(p_sub_dir))
                if i_file == FLAGS.file:
                    break

def main():
    prepare_dir()
    move_files()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b',
        '--base_dir',
        type=str,
        default='/home/i348221/Apps/python/fax/ocr/20.image/done/f1',
        help='base directory'
    )
    parser.add_argument(
        '-d',
        '--directory',
        type=int,
        default=20,
        help='Number of directory'
  )
    parser.add_argument(
        '-f',
        '--file',
        type=int,
        default=5,
        help='Number of files in a directory'
  )
    parser.add_argument(
        '-u',
        '--upload',
        type=str,
        default='fax/test/f1/',
        help='directory to upload'
    )

    FLAGS, unparsed = parser.parse_known_args()
    main()
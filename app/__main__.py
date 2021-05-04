import argparse
from app.core.main import Worker


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', help='source file', type=str)
    parser.add_argument('--d', help='target file', type=str)
    parser.add_argument('--m', help='method, possible variants '
                                    '(transpose,sum,determinant)', type=str)
    args = parser.parse_args()
    worker = Worker(args.s, args.d, args.m)
    worker.run()

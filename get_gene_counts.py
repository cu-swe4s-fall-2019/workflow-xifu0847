import os
import gzip
import argparse


def linear_search(key, L):
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


def get_parser():
    parser = argparse.ArgumentParser(description='Get Gene Counts')

    parser.add_argument('--file_name', type=str, default='',
                        help='sample_attributes file path')
    parser.add_argument('--gene_name', type=str, default='',
                        help='Gene names, such as SDHB')
    parser.add_argument('--output_file', type=str, default='Untitled.png',
                        help='output file as a .txt')

    args = parser.parse_args()
    return args


def main():
    # load args and check if they are valid
    args = get_parser()

    if not os.path.exists(args.file_name):
        raise FileNotFoundError('Gene reads file not found')
    if os.path.exists(args.output_file):
        raise FileFoundError('File has already existed')

    version = None
    dim = None
    data_header = None
    f = open(args.output_file, 'w')

    for l in gzip.open(args.file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = l.rstrip().split('\t')
            des_idx = linear_search('Description', data_header)
            continue

        A = l.rstrip().split('\t')
        if A[des_idx] == args.gene_name:
            for i in range(des_idx + 1, len(A)):
                f.write(data_header[i] + '\t' + A[i] + '\n')


if __name__ == '__main__':
    main()

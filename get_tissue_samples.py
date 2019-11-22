import os
import argparse


def linear_search(key, L):
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


def get_parser():
    parser = argparse.ArgumentParser(description='Data visualization')

    parser.add_argument('--file_name', type=str, default='',
                        help='sample_attributes file path')
    parser.add_argument('--tissue_name', type=str, default='',
                        help='Tissue names, such as Brain')
    parser.add_argument('--output_file', type=str, default='Untitled.png',
                        help='output file as a picture')

    args = parser.parse_args()
    return args


def main():
    # load args and check if they are valid
    args = get_parser()

    if not os.path.exists(args.file_name):
        raise FileNotFoundError('sample_attributes file not found')
    if os.path.exists(args.output_file):
        raise FileFoundError('File has already existed')

    sample_id_col_name = 'SAMPID'
    samples = []
    sample_info_header = None
    for l in open(args.file_name):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    group_col_idx = linear_search("SMTS", sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

    with open(args.output_file, 'w') as f:
        for sample in samples:
            sample_name = sample[sample_id_col_idx]
            curr_group = sample[group_col_idx]

            if curr_group == args.tissue_name:
                f.write(sample_name + '\n')


if __name__ == '__main__':
    main()

import os
import gzip
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def get_parser():
    parser = argparse.ArgumentParser(description='Data visualization')

    parser.add_argument('--tissues', nargs='+', type=str, default='',
                        help='A list of tissue names')
    parser.add_argument('--genes', nargs='+', type=str, default='',
                        help='A list of gene names')
    parser.add_argument('--out_file', type=str, default='Untitled.png',
                        help='output file as a figure')

    args = parser.parse_args()
    return args


def main():
    # load args and check if they are valid
    args = get_parser()

    if os.path.exists(args.out_file):
        raise FileFoundError('File has already existed')

    tissue_data = {}
    gene_data = []

    # Data Preprocessing
    for tissue in args.tissues:
        if not os.path.exists(tissue + '_samples.txt'):
            raise FileNotFoundError('Missing sample file')
        with open(tissue + '_samples.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                if tissue in tissue_data.keys():
                    tissue_data[tissue].append(line)
                else:
                    tissue_data[tissue] = [line]
            f.close()

    for gene in args.genes:
        if not os.path.exists(gene + '_counts.txt'):
            raise FileNotFoundError('Missing gene counts file')
        data = {}
        with open(gene + '_counts.txt') as f:
            for line in f:
                temp = line.rstrip('\n').split('\t')
                data[temp[0]] = int(temp[1])
            gene_data.append(data)
            f.close()

    # Plot data
    fig = plt.figure(dpi=300)
    fig_num = 1
    for tissue in args.tissues:
        all_gene = []
        for cur_gene_data in gene_data:
            cur_gene = []
            for key in cur_gene_data.keys():
                if key in tissue_data[tissue]:
                    cur_gene.append(cur_gene_data[key])
            all_gene.append(cur_gene)
        fig.add_subplot(len(args.tissues), 1, fig_num)
        plt.tight_layout()
        plt.boxplot(all_gene, labels=args.genes)
        plt.title(tissue)
        fig_num += 1
    plt.savefig(args.out_file)


if __name__ == '__main__':
    main()

#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

echo -e "\n\033[31m[Test] Style test \033[0m\n"
run Style_test_plot_gtex pycodestyle test_get_gene_counts.py get_gene_counts.py
assert_no_stdout

echo -e "\n\033[31m[Test] Functional test \033[0m\n"
run Func_test_no_file_test python get_gene_counts.py --file_name=Bad.gct.gz --gene_name=SDHB --output_file=test.txt
assert_in_stderr 'Gene reads file not found'

rm test.txt
run Func_test_good_test python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=SDHB --output_file=test.txt
assert_exit_code 0

run Func_test_txt_exist_test python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=SDHB --output_file=test.txt
assert_in_stderr 'File has already existed'
rm test.txt
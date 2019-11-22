#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Data preparetion
python get_tissue_samples.py --file_name=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tissue_name=Brain --output_file=Brain_samples.txt
python get_tissue_samples.py --file_name=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tissue_name=Heart --output_file=Heart_samples.txt
python get_tissue_samples.py --file_name=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tissue_name=Blood --output_file=Blood_samples.txt
python get_tissue_samples.py --file_name=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tissue_name=Skin --output_file=Skin_samples.txt
python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=SDHB --output_file=SDHB_counts.txt
python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=MEN1 --output_file=MEN1_counts.txt
python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=KCNH2 --output_file=KCNH2_counts.txt
python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=MSH2 --output_file=MSH2_counts.txt
python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=MYL2 --output_file=MYL2_counts.txt
python get_gene_counts.py --file_name=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene_name=BRCA2 --output_file=BRCA2_counts.txt


echo -e "\n\033[31m[Test] Style test \033[0m\n"
run Style_test_plot_gtex pycodestyle box.py --ignore=E402
assert_no_stdout

echo -e "\n\033[31m[Test] Functional test \033[0m\n"
run Func_test_bad_tissue_test python box.py --tissues Bad Brain --genes SDHB MEN1 KCNH2 MSH2 MYL2 BRCA2 --out_file=test.png
assert_in_stderr 'Missing sample file'

run Func_test_bad_tissue_test python box.py --tissues Brain Heart Blood Skin --genes Bad SDHB --out_file=test.png
assert_in_stderr 'Missing gene counts file'

rm test.png
run Func_test_good_test python box.py --tissues Brain Heart Blood Skin --genes SDHB MEN1 KCNH2 MSH2 MYL2 BRCA2 --out_file=test.png
assert_exit_code 0

run Func_test_fig_exist_test python box.py --tissues Brain Heart Blood Skin --genes SDHB MEN1 KCNH2 MSH2 MYL2 BRCA2 --out_file=test.png
assert_in_stderr 'File has already existed'
rm test.png

# Clean up
rm *_samples.txt
rm *_counts.txt
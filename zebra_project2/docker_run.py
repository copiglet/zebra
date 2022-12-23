import os

PATH = "/home/phenomx/dante/zebra/zebra_project2"
cmd = 'docker run --rm -it \
                --gpus=all \
                --name zebra_test \
                -v {0}/input:/workspace/input:rw \
                -v {0}/cropped_egg:/workspace/cropped_egg:rw \
                -v {0}/detect_infer:/workspace/detect_infer:rw \
                -v {0}/final_larva:/workspace/final_larva:rw \
                -v {0}/output.csv:/workspace/output.csv:rw \
                -v {0}/run_script:/workspace/run_script:rw \
                -v {0}/run.py:/workspace/run.py:rw \
                zebra:v1'.format(PATH)
os.system(cmd)
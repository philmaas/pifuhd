
python ../lightweight-human-pose-estimation.pytorch/crop_imagePose.py

python -m apps.simple_test -r 512 --use_rect -i ./sample_images/

python apps/clean_mesh.py -f ./results/pifuhd_final/recon/
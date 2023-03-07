
python ../lightweight-human-pose-estimation.pytorch/crop_imagePose.py

python -m apps.simple_test -r 512 --use_rect -i ./sample_images/

python apps/clean_mesh.py -f ./results/pifuhd_final/recon/


python -m apps.render_turntable -f ./results/pifuhd_final/recon/ -ww 512 -hh 512
# add -g for geometry rendering. default is normal visualization.
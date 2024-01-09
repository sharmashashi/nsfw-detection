mkdir output_frames
ffmpeg -i video_sample.mp4 -vf fps=30 output_frames/frame-%04d.png
python3 nudenet_example.py
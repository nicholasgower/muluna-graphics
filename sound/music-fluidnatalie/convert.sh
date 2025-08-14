for f in *.wav; do
    ffmpeg -y -i "$f" -c:a libvorbis "${f%.wav}.ogg"
done

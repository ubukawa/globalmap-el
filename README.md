# globalmap-el
Working directory to convert global map elevation into RGB tiles

# sources
Global Map Elevation - version 2  
https://github.com/globalmaps/gm_el_v2_west  
https://github.com/globalmaps/gm_el_v2_east  

# unvt/rgbify
```
git clone https://github.com/unvt/rgbify
cd rgbify
docker build -t unvt/rgbify .
cd ..

docker run -it --rm -v ${PWD}:/data unvt/rgbify
cd /data
```

# Work flow
See https://qiita.com/T-ubu/items/ced8423e0ebeda8c9244 (in Japanese, use translation)
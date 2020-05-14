img=imread('cameraman.tif');
[Gx,Gy]=imgradientxy(img,'sobel');
imshowpair(Gx,Gy,'montage')
[Gmag,Gdir] = imgradient(Gx,Gy);
imshowpair(Gmag,Gdir,'montage')

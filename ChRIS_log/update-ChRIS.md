

```
docker pull fnndsc/pl-matmultiply

docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=1 robertmorrislike/pl-matmultiply python3 matmultiply.py in out
```

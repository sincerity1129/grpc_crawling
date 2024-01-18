# grpc
### -I 프로트 파일 있는 경로 
### --python_out, --pyi_out, --grpc_python_out 세팅 후 기본 파일 생성 경로
### 프로토 파일 경로
    python -m grpc_tools.protoc -I./proto --python_out=./pb2file --pyi_out=./pb2file --grpc_python_out=./pb2file ./proto/crawler.proto